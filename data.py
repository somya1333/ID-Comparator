import io
import os
import pandas as pd
import numpy as np
from google.cloud import vision


credential_path = r'C:\Users\ACER\Desktop\vision api\client.json' 
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


name = "NAME"
DOB = "DOB"
PAN = "PERMANENT ACCOUNT NUMBER CARD"
aadhar = "AADHAR NO"
DL_number = "DLNUMBER"
gaurdian_name = "FATHER'S NAME"
gender = "GENDER"
mobile = "MOBILE"
none = "none"


def read_text(image_file):
    
    client_data_list = ["type",
            "first_name",
            "last_name",
            "father_name",
            "dob",
            "gender",
            "email",
            "mobile",
            "pan_no",
            "aadhar_number",
            "DL_Number" ]

    client_data = dict.fromkeys(client_data_list)

    client = vision.ImageAnnotatorClient()
    with io.open(image_file, 'rb') as image_file:
            content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print(type(texts))
    for text in texts:

        # print((text))
        text_data = text.description.upper()
        print((text_data))
        # agents name
        if name in text_data:
            start = text_data.find(name)+len(name)+1
            end=start
            while text_data[end]!='\n' and end<len(text_data)-1:
                end+=1
            client_data["first_name"] = text_data[start:end]
            start=end+1
            while text_data[end]!='\n':
                end+=1
            client_data["last_name"] = text_data[start:end]
        else:
            client_data["first_name"] = none
            client_data["last_name"] = none

        # Father's name
        if gaurdian_name in text_data:
            start = text_data.find(gaurdian_name)+len(gaurdian_name)+1

            end=start
            while text_data[end]!='\n' and end<len(text_data):
                end+=1
            client_data["father_name"] = text_data[start:end]
        else:
            client_data["father_name"] = none
            
        # PAN number
        if PAN in text_data:
            start = text_data.find(PAN)+len(PAN)+1
            end=start
            while text_data[end]!='\n' and end<len(text_data):
                end+=1
            client_data["pan_no"] = text_data[start:end]
            client_data["type"] = ("PAN CARD")
        else:
            client_data["pan_no"] = none

        # DOB
        if DOB in text_data:
            start = text_data.find(DOB)+len(DOB)+1
            end=start
            while text_data[end]!='\n' and end<len(text_data):
                end+=1
            client_data["dob"] = text_data[start:end]
        else:
            client_data["dob"] = none

        # Driving License number
        if DL_number in text_data:
            start = text_data.find(DL_number)+len(DL_number)+1
            end=start
            while text_data[end]!='\n' and end<len(text_data):
                end+=1
            client_data["DL_Number"] = text_data[start:end]
            client_data["type"] = ("DRIVING LICENSE")
        else:
            client_data["DL_Number"] = none

        # Aadhar number
        if aadhar in text_data:
            start = text_data.find(aadhar)+len(aadhar)+1
            end=start
            while text_data[end]!='\n' and end<len(text_data):
                end+=1
            client_data["aadhar_number"] = text_data[start:end]
        else:
            client_data["aadhar_number"] = none
        break

    if response.error.message:
        raise Exception(f'{response.error.message}')
    
    return client_data