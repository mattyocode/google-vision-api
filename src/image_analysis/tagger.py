from __future__ import print_function
import os
import json

from google.cloud import vision

image_uri = 'https://drive.google.com/file/d/1B7WmDp4R96G_gQEYje32wAe3ZRcqHIK0/view?usp=sharing'

path = os.path.abspath(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])

client = vision.ImageAnnotatorClient.from_service_account_json(path)
image = vision.Image()
image.source.image_uri = image_uri

response = client.label_detection(image=image)

print('Labels (and confidence score):')
print('=' * 30)
for label in response.label_annotations:
    print(label.description, '(%.2f%%)' % (label.score*100.))