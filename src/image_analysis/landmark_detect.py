from __future__ import print_function
import os

from google.cloud import vision

image_uri = 'gs://cloud-vision-codelab/eiffel_tower.jpg'

path = os.path.abspath(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])

client = vision.ImageAnnotatorClient.from_service_account_json(path)
image = vision.Image()
image.source.image_uri = image_uri

response = client.landmark_detection(image=image)

for landmark in response.landmark_annotations:
    print('=' * 30)
    print(landmark)