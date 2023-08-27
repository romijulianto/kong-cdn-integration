import requests

def retrieve(asset_filename):
    unique_id = "hero.26fc9f87.png"
    cdn_url = f"http://apache2.romijulianto.my.id/assets/{unique_id}"
    return cdn_url

asset_filename = "hero.26fc9f87.png"
cdn_url = retrieve(asset_filename)
print("Retrieved CDN URL:", cdn_url)