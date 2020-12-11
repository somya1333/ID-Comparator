from __future__ import print_function, unicode_literals
import json
from facepplib import FacePP, exceptions

api_key = "2GD4vbXSFV56Bq_mbhjVFxipMYkTY3z5"
api_secret = "B2r5UwYYkT8jJjWuk-wGk2lx9IqLAv5v"
app = FacePP(api_key=api_key,api_secret=api_secret)

def face_comparing(image_url1, image_url2):
    image_cmp = app.compare.get(image_url1=image_url1,image_url2=image_url2)
    return image_cmp.confidence