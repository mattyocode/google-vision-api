from __future__ import print_function
import os

from google.cloud import vision

image_uri = 'gs://cloud-vision-codelab/otter_crossing.jpg'

path = os.path.abspath(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])

client = vision.ImageAnnotatorClient.from_service_account_json(path)
image = vision.Image()
image.source.image_uri = image_uri

response = client.text_detection(image=image)

for text in response.text_annotations:
    print('=' * 30)
    print(text.description)
    vertices = ['(%s,%s)' % (v.x, v.y) for v in text.bounding_poly.vertices]
    print('bounds:', ",".join(vertices))