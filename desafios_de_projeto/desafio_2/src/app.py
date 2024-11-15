import streamlit as st
import tempfile
from services.credit_card_service import detect_credit_card_info    
from services.blob_service import upload_to_blob
from services.data_base import DataBase
import datetime as dt



def display_credit_card_info(credit_card_info):
    is_valid = bool(
        credit_card_info["IssuingBank"] and
        credit_card_info["CardHolderName"] and
        credit_card_info["CardNumber"] and
        credit_card_info["ExpirationDate"]
    )
    st.markdown(f"<h1 style='color: {'green' if is_valid else 'red'};'>Cartão {'Válido' if is_valid else 'Inválido'}</h1>", unsafe_allow_html=True)
    st.write(f"Nome do Titular: {credit_card_info['CardHolderName']}")
    st.write(f"Banco Emissor: {credit_card_info['IssuingBank']}")
    st.write(f"Número do Cartão: {credit_card_info['CardNumber']}")
    st.write(f"Data de Validade: {credit_card_info['ExpirationDate']}")

    return is_valid

def save_card_info(credit_card_info):
    db = DataBase()
    card_number = credit_card_info["CardNumber"]
    existing_card = db.get_card_by_number(card_number)
    if existing_card:
        st.success(f"O cartão com o número {card_number} já existe no banco de dados e é válido.")
    else:
        card_info = {
            "card_name": credit_card_info["CardHolderName"],
            "card_number": credit_card_info["CardNumber"],
            "expiry_date": credit_card_info["ExpirationDate"],
            "bank_name": credit_card_info["IssuingBank"],
            "is_valid": "true" if all(credit_card_info.values()) else "false",
            "processed_at": str(dt.datetime.now())
        }
        db.insert_card(card_info)
        st.success("Informações do cartão salvas no banco de dados!")

def configure_interface():
    st.title("Análise Anti-fraude de cartão de crédito com AzureAI")
    # Carregar o arquivo de imagem
    uploaded_file = st.file_uploader("Escolha uma imagem", type=['png', 'jpg', 'jpeg'])
    if uploaded_file is not None:        
        try:
            # Criar um arquivo temporário para armazenar a imagem
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                temp_file.write(uploaded_file.getvalue())  # Salvar conteúdo no arquivo temporário
                temp_file_path = temp_file.name            
            # Fazer o upload usando o caminho do arquivo temporário
            blob_url = upload_to_blob(temp_file_path, uploaded_file.name)            
            # Remover o arquivo temporário
            temp_file.close()            
            st.success('Upload realizado com sucesso para o Azure Blob Storage!')
            credit_card_info = detect_credit_card_info(blob_url)
            if credit_card_info:
                is_valid = display_credit_card_info(credit_card_info)
                if is_valid:
                    save_card_info(credit_card_info)
            else:
                st.error("Não foi possível detectar informações do cartão na imagem")

        except Exception as e:
            st.error(f"Erro durante o upload: {str(e)}")

def database_menu():
    st.title("Consulta Banco de Dados")
    db = DataBase()
    
    # Mostrar estatísticas básicas
    cards = db.get_all_cards()
    st.subheader("Estatísticas do Banco de Dados")
    st.write(f"Total de cartões cadastrados: {len(cards)}")
    valid_cards = sum(1 for card in cards if card['is_valid'] == 'true')
    st.write(f"Cartões válidos: {valid_cards}")
    st.write(f"Cartões inválidos: {len(cards) - valid_cards}")
    
    # Mostrar todos os registros
    with st.expander("Ver todos os registros"):
        if cards:
            st.write(cards)
        else:
            st.write("Não há cartões cadastrados no momento.")
    
    # Consulta personalizada
    with st.expander("Consulta Personalizada"):
        st.write("""
        Exemplos de consultas:
        - SELECT * FROM credit_cards WHERE is_valid = 'true'
        - SELECT bank_name, COUNT(*) as total FROM credit_cards GROUP BY bank_name
        - SELECT * FROM credit_cards WHERE processed_at LIKE '%2024%'
        """)
        
        query = st.text_area("Digite sua consulta SQL (apenas SELECT):")
        if st.button("Executar Consulta"):
            try:
                result = db.execute_custom_query(query)
                st.write(result)
            except Exception as e:
                st.error(f"Erro ao executar a consulta: {str(e)}")

def main():
    st.set_page_config(page_title="Análise Anti-fraude de Cartão de Crédito")
    pages = {
        "Análise de Cartão de Crédito": configure_interface,
        "Consulta Banco de Dados": database_menu
    }
    st.sidebar.title("Menu")
    selection = st.sidebar.radio("Navegue para a opção desejada", list(pages.keys()))
    pages[selection]()

if __name__ == "__main__":
    main()