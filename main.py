import firebase_admin
from firebase_admin import credentials, storage
import pyrebase
import requests

config = {
    "apiKey": "AIzaSyCzN1i27BpL1SbSZotH32zTBgWnaE4N-QA",
    "authDomain": "first-project-2a299.firebaseapp.com",
    "projectId": "first-project-2a299",
    "storageBucket": "first-project-2a299.appspot.com",
    "messagingSenderId": "35008157681",
    "appId": "1:35008157681:web:3908d06fe7751234e21650",
    "measurementId": "G-ET6CRXDV6L",
    "serviceAccount": "first-project-private-key-firebase-adminsdk.json",
    "databaseURL": "https://first-project-2a299-default-rtdb.firebaseio.com/"
}


firebase = pyrebase.initialize_app(config)
storage = firebase.storage()


def upload_image(local_file_path, destination_blob_name):
    storage.child(destination_blob_name).put(local_file_path)
    
    # Trả về URL của hình ảnh sau khi upload
    url = storage.child(destination_blob_name).get_url(None)
    print(f"File {local_file_path} uploaded to {destination_blob_name}")
    print(f"Image URL: {url}")
    return url

def download_image(url, destination_file_path):
    response = requests.get(url)
    with open(destination_file_path, 'wb') as file:
        file.write(response.content)
    print(f"Image downloaded to {destination_file_path}")


# Ví dụ sử dụng
image_url = upload_image("VietnamDatathon_FunnyIUH.png", "picture/image.png")

# Download ảnh
download_image(image_url, "download_test2.png")

# Xóa ảnh
# delete_image("picture/image.png")
