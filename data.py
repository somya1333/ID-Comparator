import io
import os
import pandas as pd
import numpy as np
from google.cloud import vision


credential_path = r'C:\Users\ACER\Desktop\vision api\client.json' 
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

search_data = [
    name = "NAME",
    DOB = "DOB",
    gaurdian_name = "FATHER'S NAME",
    gender = "GENDER",
    mobile = "MOBILE",
]

search_type = [
    PAN = "PERMANENT ACCOUNT NUMBER CARD",
    aadhar = "AADHAR NO",
    DL_number = "DLNUMBER"
]


# Function to search type of id_card
def get_type(text_data):
    for s_type in search_type:
        if s_type in text_data:
            return s_type
    return "none"

# Function to retrieve all data from id_card
def read_text(image_file):
    
    client_data_list = ["type",
            "name",
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
        
        for entity in search_data:
            
            # If data is available in identity card
            if entity in text_data:
               start = text_data.find(entity)+len(entity)+1
                end=start
                while text_data[end]!='\n' and end<len(text_data):
                    end+=1
                client_data[entity] = text_data[start:end]
            else:
                client_data[entity] = "none"
            
        # Finding the type of id_card
        client_data["type"] = get_type(text_data)
        break

    if response.error.message:
        raise Exception(f'{response.error.message}')
    
    return client_data
