import os
import uuid
# Import the client object from the SDK library
from azure.storage.blob import BlobClient

def blob(data):

    # Retrieve the connection string from an environment variable. Note that a connection
    # string grants all permissions to the caller, making it less secure than obtaining a
    # BlobClient object using credentials.
    conn_string = os.environ["AZURE_STORAGE_CONNECTION_STRING"]
    hoge_id = str(uuid.uuid4())
    print(conn_string)

    # Create the client object for the resource identified by the connection string,
    # indicating also the blob container and the name of the specific blob we want.
    blob_client = BlobClient.from_connection_string(conn_string,
        container_name="blob1", blob_name=hoge_id+".png")

    # Open a local file and upload its contents to Blob Storage
    # with open("./sample-source.txt", "rb") as data:
    a = blob_client.upload_blob(data)
    print (a)
    return "https://omotimotti.blob.core.windows.net/blob1/" + hoge_id+".png"