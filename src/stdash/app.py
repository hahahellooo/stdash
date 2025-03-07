import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import datetime as dt

st.title('CNN JOB MON')

def load_data():
    url = 'http://43.202.66.118:8077/all'
    r = requests.get(url)
    d = r.json()
    return d

data = load_data()
df = pd.DataFrame(data)

df['request_time'] = pd.to_datetime(df['request_time'])
df['request_time']=df['request_time'].dt.strftime('%Y-%m-%d %H')
df['prediction_time'] = pd.to_datetime(df['prediction_time'])
df['prediction_time']=df['prediction_time'].dt.strftime('%Y-%m-%d %H')

cnt_rt = df.groupby(df['request_time']).size()
cnt_pt = df.groupby(df['prediction_time']).size()

# 막대 그래프: 요청 시간별 건수
plt.bar(cnt_rt.index, cnt_rt, color='#ebf301', label='Request Time', alpha=0.8) # alpha 투명도 조절

# 선 그래프: 예측 시간별 건수
plt.plot(cnt_pt.index, cnt_pt, 'ro-', label='Prediction Time') # r 선의 색상, o 포인트 마커모양

# 그래프 설정
plt.title('Requests by Date and Time')
plt.xlabel('Date and Time')
plt.ylabel('Number Of Requests')
plt.xticks(rotation=45)  # X축 레이블 회전 (텍스트가 길 경우)
plt.legend()

# 그래프 출력
st.pyplot(plt)
