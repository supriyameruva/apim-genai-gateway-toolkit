from flask import Flask, render_template, request
from azure.storage.blob import BlobServiceClient
import os

app = Flask(__name__)

# Initialize Blob Service Client using connection string
connection_string = os.getenv("BlobEndpoint=https://storagerrg01.blob.core.windows.net/;QueueEndpoint=https://storagerrg01.queue.core.windows.net/;FileEndpoint=https://storagerrg01.file.core.windows.net/;TableEndpoint=https://storagerrg01.table.core.windows.net/;SharedAccessSignature=sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2024-10-13T02:48:44Z&st=2024-10-12T18:48:44Z&spr=https&sig=WRYKjWLhLf27H%2BA%2BuO2iMwJ2G7HHFUB7Hy8gS92etCI%3D")
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_name = 'mywebblob'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file.filename)
    blob_client.upload_blob(file)
    return f"File {file.filename} uploaded successfully!"

if __name__ == '__main__':
    app.run(debug=True)
