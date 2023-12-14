import firebase_admin
from firebase_admin import credentials, storage

# Khởi tạo Firebase Admin SDK
cred = credentials.Certificate("first-project-private-key-firebase-adminsdk.json")
firebase_admin.initialize_app(cred, {'storageBucket': 'first-project-2a299.appspot.com'})

def upload_image(local_file_path, destination_blob_name):
    bucket = storage.bucket()
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(local_file_path)
    
    # Trả về URL của hình ảnh sau khi upload
    url = blob.public_url
    print(f"File {local_file_path} uploaded to {destination_blob_name}")
    print(f"Image URL: {url}")
    return url

def download_image(destination_file_path, source_blob_name):
    bucket = storage.bucket()
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_path)
    print(f"File {source_blob_name} downloaded to {destination_file_path}")

def delete_image(source_blob_name):
    bucket = storage.bucket()
    blob = bucket.blob(source_blob_name)
    blob.delete()
    print(f"File {source_blob_name} deleted from Firebase Storage")


# Ví dụ sử dụng
image_url = upload_image("VietnamDatathon_FunnyIUH.png", "picture/image3.png")

# Download ảnh
download_image("download_test4.png", "picture/image3.png")

# Xóa ảnh
delete_image("picture/image3.png")
