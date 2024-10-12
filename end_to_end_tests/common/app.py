from flask import Flask, request, render_template, redirect, url_for
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

app = Flask(__name__)

# Azure Blob Storage settings (Replace these with your values)
STORAGE_ACCOUNT_NAME = os.getenv('storagerrg01')
CONTAINER_NAME = os.getenv('mywebblob')
SAS_TOKEN = os.getenv('sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2024-10-13T02:48:44Z&st=2024-10-12T18:48:44Z&spr=https&sig=WRYKjWLhLf27H%2BA%2BuO2iMwJ2G7HHFUB7Hy8gS92etCI%3D')

# Initialize the BlobServiceClient
blob_service_client = BlobServiceClient(
    account_url=f"https://storagerrg01.blob.core.windows.net", 
    credential=SAS_TOKEN
)

# Upload file to Azure Blob Storage
@app.route('/upload_blob', methods=['POST'])
def upload_blob():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    try:
        # Create a BlobClient
        blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=file.filename)

        # Upload the file to Blob Storage
        blob_client.upload_blob(file)
        return f"File {file.filename} uploaded to Blob Storage successfully!"
    except Exception as e:
        return f"Failed to upload file to Blob Storage: {e}"

# Example route to render a file upload form
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
