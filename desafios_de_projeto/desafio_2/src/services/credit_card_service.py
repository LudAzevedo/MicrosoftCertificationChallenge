import pandas as pd
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.core.credentials import AzureKeyCredential
from utils.Config import Config


def detect_credit_card_info(card_url):
    """
    Extrai informações de um catão de crédito

    Args:
        card_url: url de uma imagem de cartão de crédito

    Return:
        Um dataframe com as informações do cartão de crédito
    """
    credential = AzureKeyCredential(Config.KEY)
    document_client = DocumentIntelligenceClient(Config.ENDPOINT, credential)
    card_info = document_client.begin_analyze_document(
        "prebuilt-creditCard", AnalyzeDocumentRequest(url_source=card_url)
    )
    result = card_info.result()

    # Extract fields from the first document (assuming one card per image)
    fields = result.documents[0].get("fields", {})

    # Flatten the nested dictionary to a simple dictionary
    result = {}
    for key, value in fields.items():
        if "valueArray" in value:
            # Handle arrays of values
            result[key] = [v["valueString"] for v in value["valueArray"]]
        else:
            result[key] = value["content"]

    # Create a Pandas DataFrame from the flattened dictionary
    #df = pd.DataFrame.from_dict(result, orient="index", columns=["value"])

    return result
