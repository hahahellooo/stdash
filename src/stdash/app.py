import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import datetime as dt
import os

st.title('CNN JOB MON')

def load_data():
    url = 'http://43.202.66.118:8077/all'
    r = requests.get(url)
    d = r.json()
    return d
st.sidebar.title('Analysis')

data = load_data()
df = pd.DataFrame(data)
df

def graph_time():

    df['request_time'] = pd.to_datetime(df['request_time'])
    df['request_time']=df['request_time'].dt.strftime('%Y-%m-%d %H')
    df['prediction_time'] = pd.to_datetime(df['prediction_time'])
    df['prediction_time']=df['prediction_time'].dt.strftime('%Y-%m-%d %H')

    cnt_rt = df.groupby(df['request_time']).size()
    cnt_pt = df.groupby(df['prediction_time']).size()

    # 선 그래프: 예측 시간별 건수
    plt.plot(cnt_pt.index, cnt_pt, 'ro-', label='Prediction Time') # r 선의 색상, o 포인트 마커모양

    # 막대 그래프: 요청 시간별 건수
    plt.bar(cnt_rt.index, cnt_rt, color='#ebf301', label='Request Time', alpha=0.8) # alpha 투명도 조절

    # 그래프 설정
    # 한국어로 설정시 따로 폰트설정 필요
    plt.title('Requests by Date and Time')
    plt.xlabel('Date and Time')
    plt.ylabel('Number Of Requests')
    plt.xticks(rotation=45)  # X축 레이블 회전 (텍스트가 길 경우)
    plt.legend()
# 그래프 출력
    st.pyplot(plt)

if st.sidebar.button('Step1'):
   graph_time()

def graph_user():
    df2 = df.groupby(df['request_user']).size()
    df4 = df.groupby(df['prediction_model']).size()
    df2_sorted = df2.sort_index(ascending=True)
    df4_sorted = df4.sort_index(ascending=True)
    plt.plot(df4_sorted.index, df4_sorted, 'ro-', label = 'request user')
    plt.bar(df2_sorted.index, df2_sorted, color='#ebf301', label = 'prediction model')
    plt.title('Requests by User and Prediction Model')
    plt.xlabel('Request User and Prediction Model')
    plt.ylabel('Number Of Requests')
    plt.xticks(rotation=45, ha='right')  # X축 레이블 회전 (텍스트가 길 경우) # ha = 'right' 레이블이 오른쪽정렬
    plt.legend()

# 그래프 출력
    st.pyplot(plt)

if st.sidebar.button('Step2'):
    graph_user()

def upload_file():
    url = "http://43.202.66.008:8021/uploadfile/"
    img_file = st.file_uploader('Upload your image file here🤗', type=['png','jpg','jpeg'])
    if img_file is not None:
        files = {"file":(img_file.name, img_file.getvalue(), img_file.type)}
        response = requests.post(url, files=file)
        if response.status_code == 200:
            st.success("🎉Image uploaded successfully🎉")
            st.write(response.json())
        else:
            st.error(f"Upload failed, Please upload your image again (Error Code:{response.status_code})")
            st.write(response.text)

if st.sidebar.button('Step3'):
    upload_file()

