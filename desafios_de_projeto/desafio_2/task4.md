

# TASK 4: 

**Tarefa 4: Sistema de validação**

* [x] Criar a funçao para realizar o upload e extrair as informações do cartão.
* [x] Criar a função de validação.
* [x] Realizar testes com exemplos.

## Sistema de validação

* **Primeiro passo é importar as libs e métodos:**


```python
from utils.Config import Config 
from services.blob_service import upload_to_blob
from services.credit_card_service import detect_credit_card_info
from services.data_base import DataBase 
import streamlit as st 
```

* **Criar a funçao para realizar o upload e extrair as informações do cartão**:


```python
def upload_and_check_credit(path, filename=None):
    url = upload_to_blob(path, filename)
    if url is not None:
        card_info = detect_credit_card_info(url)
        return card_info
    else:
        print("não foi possível realizar o upload")

```

* **Vamos verificar se a função está funcional:**


```python
path = "../img/exemplo.jpg"
upload_and_check_credit(path)
```




    {'CardHolderName': 'M. Molina'}



* **Agora precisamos criar uma função de validação que faça:**
    - receba os resultados do cartão, verifique e valide se possui as informações necessárias de um cartão de crédito.
    - Informe se o cartão é válido ou não e retorne os valores obtidos


```python
def display_credit_card_info(credit_card_info): 
    # Verifica se as chaves existem, se não existirem retorna None
    issuing_bank = credit_card_info.get('IssuingBank')
    card_holder = credit_card_info.get('CardHolderName')
    card_number = credit_card_info.get('CardNumber')
    expiration_date = credit_card_info.get('ExpirationDate')
    # Verifica se todos os campos necessários estão presentes e não são None
    is_valid = all([issuing_bank, card_holder, card_number, expiration_date])
    print(f"Cartão {'Válido' if is_valid else 'Inválido'}")
    # Exibe as informações com substituição de "Não detectado" para campos ausentes
    print(f"Nome do Titular: {card_holder if card_holder else 'Não detectado'}")
    print(f"Banco Emissor: {issuing_bank if issuing_bank else 'Não detectado'}")
    print(f"Número do Cartão: {card_number if card_number else 'Não detectado'}")
    print(f"Data de Expiração: {expiration_date if expiration_date else 'Não detectado'}")
    
    
```


```python
credit_card_info = upload_and_check_credit("../img/exemplo.jpg") 
display_credit_card_info(credit_card_info)
```

    Cartão Inválido
    Nome do Titular: M. Molina
    Banco Emissor: Não detectado
    Número do Cartão: Não detectado
    Data de Expiração: Não detectado


![img](./img/exemplo.jpg)

* **Beleza, como podem ver o cartão não possui todos os requisitos e portanto não foi validado!**
* **Bora testar um exemplo de cartão válido agora.**

![card](./img/nubank.jpg)


```python
credit_card_info = upload_and_check_credit("../img/nubank.jpg") 
display_credit_card_info(credit_card_info)
```

    Cartão Válido
    Nome do Titular: GABRIEL LIMA
    Banco Emissor: ny
    bank
    Número do Cartão: 5032 9334 3764 9846
    Data de Expiração: 09/17


![img](./img/multimoneda.png)


```python
credit_card_info = upload_and_check_credit("../img/multimoneda.png") 
display_credit_card_info(credit_card_info)
```

    Cartão Válido
    Nome do Titular: MANUEL GARCIA
    Banco Emissor: Multimoneda
    BANRESERVAS
    Número do Cartão: 5227 1234 1234 1234
    Data de Expiração: 12/22

