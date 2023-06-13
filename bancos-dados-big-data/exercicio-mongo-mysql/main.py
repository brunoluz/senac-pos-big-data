import mysql.connector
import pandas as pd
from PIL import Image
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import io
import matplotlib.pyplot as plt

client = MongoClient()
db = client.senac

collection = db.NovaCollection1
result = collection.find_one({'x': 1})
print(result)

im = Image.open("image.jpg")
image_bytes = io.BytesIO()

im.save(image_bytes, format='JPEG')

image = {
    'data': image_bytes.getvalue()
}
image_id = db.images.insert_one(image).inserted_id
client = MongoClient()
db = client.senac

images = db.images
image = images.find_one()
pil_img = Image.open(io.BytesIO(image['data']))
plt.imshow(pil_img)
plt.show()


