from azure.storage.blob import BlobServiceClient, ResourceExistsError

# Set up your connection details
sas_token = "sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2024-10-15T00:11:45Z&st=2024-10-10T16:11:45Z&spr=https&sig=8bz9USkB5%2BMDy1PP1iSGy3Ad0%2BUF2UidSgPNdC2T96Y%3D"  # Replace with your SAS token
storage_account_url = "https://storagerrg01.blob.core.windows.net"
container_name = "mywebapp"  # Replace with your container name

# Create BlobServiceClient using the SAS Token
blob_service_client = BlobServiceClient(account_url=storage_account_url, credential=sas_token)

def upload_file_to_blob(file_stream, file_name):
    try:
        # Create a container client
        container_client = blob_service_client.get_container_client(container_name)
        
        # Create the container if it doesn't exist
        try:
            container_client.create_container()
        except ResourceExistsError:
            pass  # Ignore if the container already exists

        # Create a BlobClient to interact with the blob
        blob_client = container_client.get_blob_client(file_name)

        # Upload the file stream to Blob Storage
        blob_client.upload_blob(file_stream, overwrite=True)
        print(f"File {file_name} uploaded to Blob Storage successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
