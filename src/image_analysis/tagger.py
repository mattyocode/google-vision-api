from __future__ import print_function
import os

from google.cloud import vision

image_uri = 'gs://cloud-samples-data/vision/using_curl/shanghai.jpeg'
path = os.path.abspath(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])
print('path', path)

client = vision.ImageAnnotatorClient.from_service_account_json(path)
image = vision.Image()
image.source.image_uri = image_uri

response = client.label_detection(image=image)

print('Labels (and confidence score):')
print('=' * 30)
for label in response.label_annotations:
    print(label.description, '(%.2f%%)' % (label.score*100.))