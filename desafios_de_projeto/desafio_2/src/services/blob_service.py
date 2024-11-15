# src/services/blob_service.py
from azure.storage.blob import BlobServiceClient
from utils.Config import Config

def upload_to_blob(source, filename=None) -> str:
    """
    Faz o upload de uma imagem para o Azure Blob Storage

    Args:
        source: imagem com o caminho completo. ex:"img/imagem.png"
        filename:Nome opcional para o arquivo.

    Returns:
        str: URL do blob
    """
    if not filename:
        file = source.split(".")[0].split("/")[-1]
        extension = source.split(".")[-1]
        filename = f"{file}.{extension}"

    # Upload para o blob
    blob_service_client = BlobServiceClient.from_connection_string(
        Config.STORAGE_CONNECTION
    )
    blob_client = blob_service_client.get_blob_client(Config.CONTAINER_NAME, filename)
    with open(file=source, mode="rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    return blob_client.url
