from __future__ import print_function, unicode_literals
import json
from facepplib import FacePP, exceptions

# add your Face++ api key and secret
api_key = ""
api_secret = ""
app = FacePP(api_key=api_key,api_secret=api_secret)

def face_comparing(image_url1, image_url2):
    image_cmp = app.compare.get(image_url1=image_url1,image_url2=image_url2)
    return image_cmp.confidence
