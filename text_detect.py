import pandas as pd
import numpy as np
import glob, os
from face_comparision import face_comparing
from data import read_text
from agent_data import get_agent_data

if __name__=='__main__':

    image_file1=r''
    image_file2=r''
    image_url1 = ""
    image_url2 = ""
    # read_text(image_file1)
    # agent_data_list=[]
    agent_data={}
    # for file in os.listdir("video_data\\"):
    #     # if file.endswith("*.jpg"):
    #     file_name = os.path.join("video_data/", file)
    #     print(file_name)
    #     pan_data = read_text(file_name)
    #     agent_data_list.append(pan_data)

    # for d in agent_data_list:
    #     for k, v in d.items():
    #         agent_data.setdefault(k, []).append(v)
    dl_data = read_text(image_file1)
    pan_data = read_text(image_file2)
    # agent_data.update(pan_data)
    # agent_data.update(dl_data)

    # print(agent_data)
    # print(pan_data)
    # print(dl_data)
    confidence = face_comparing(image_url1, image_url2)
    pan_data["confidence"] = confidence
    dl_data["confidence"] = confidence

    # agent_data
    # agent_data = get_agent_data()

    for key in pan_data:
        if pan_data[key] == dl_data[key] or pan_data[key]=='none' or dl_data[key]=='none':
            agent_data[key]=[pan_data[key], dl_data[key], "Ok"]
        else:
            agent_data[key]=[pan_data[key], dl_data[key], "No"]
    
    # print(agent_data)

    df=pd.DataFrame(agent_data)
    print(df)
