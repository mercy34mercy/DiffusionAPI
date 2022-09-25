import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import uuid
import os

def firestorage(data):
    cred = credentials.Certificate('./omoti.json')

    try:
        firebase_admin.initialize_app(cred, {
            'storageBucket': os.environ["FIRE_STORAGE"]
        })
    except:
        print("allredady")

    

    hoge_id = str(uuid.uuid4())

    bucket = storage.bucket()
    content_type = 'image/png'

    blob = bucket.blob("blob/" + hoge_id + ".png")
    blob.upload_from_string(data,content_type=content_type)
    blob.make_public()
    return blob.public_url


