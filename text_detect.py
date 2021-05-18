import pandas as pd
import numpy as np
import glob, os
from face_comparision import face_comparing
from data import read_text
from agent import get_agent_data

if __name__=='__main__':
    # print("hie")
    image_file1=r'resources\somya_Aadhar.jpeg'
    image_file2=r'resources\somya_PAN.jpeg'
    image_url1 = "https://i.postimg.cc/rpzNHBBk/somya-Aadhar.jpg"
    image_url2 = "https://i.postimg.cc/C5NV2n8d/somya-PAN.jpg"

    # Aadhar card data
    aadhar_data = read_text(image_file1)

    #PAN Card data
    pan_data = read_text(image_file2)

    # for d in agent_data_list:
    #     for k, v in d.items():
    #         agent_data.setdefault(k, []).append(v)
    # agent_data.update(pan_data)
    # agent_data.update(aadhar_data)

    # print(agent_data)
    # print(pan_data)
    # print(aadhar_data)

    # Similarity between the images
    confidence = face_comparing(image_url1, image_url2)
    print(confidence)

    # agent_data
    agent_data = get_agent_data()

    for key in pan_data:
        if pan_data[key] == agent_data[key]:
            agent_data[key]="Ok"
        else:
            agent_data[key]=[pan_data[key], aadhar_data[key], "No"]
    agent_data["Confidence"] = confidence
    
    # print(agent_data)

    df=pd.DataFrame(agent_data)
    print(df)