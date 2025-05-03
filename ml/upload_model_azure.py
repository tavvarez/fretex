from azure.storage.blob import BlobServiceClient;
import os;

connect_string = os.getenv('CONNECT_STRING')
container_name = "modelov1";
blob_name = "modelo_random_forest.pkl";
local_file = "ml/modelo_random_forest.pkl";

blob_service_client = BlobServiceClient.from_connection_string(connect_string)
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name);

with open(local_file, "rb") as data:
    blob_client.upload_blob(data, overwrite=True);

print(f"Modelo enviado para azure Blobl: {container_name}/{blob_name}")