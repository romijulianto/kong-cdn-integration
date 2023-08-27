import requests

def upload(file_path):
    unique_id = "NIKE00120232708"
    upload_url = "http://localhost:8000/cdn-assets"

    response = requests.post(upload_url, files={'file': open(file_path, 'rb')})

    if response.status_code == 201:
        cdn_url = f"http://apache2.romijulianto.my.id/assets/{unique_id}"
        return cdn_url
    else:
        return None

file_path = "../assets/nike-001.png"
cdn_url = upload(file_path)

if cdn_url:
    print("Uploaded CDN URL:", cdn_url)
else:
    print("Upload failed.")