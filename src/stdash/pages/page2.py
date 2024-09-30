import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import datetime as dt
import os
st.markdown("# Request and Prediction User")                                               
st.sidebar.markdown("# Request and Prediction User")
def load_data():
    url = 'http://43.202.66.118:8077/all'
    r = requests.get(url)
    d = r.json()
    return d

data = load_data()
df = pd.DataFrame(data)

df2 = df.groupby(df['request_user']).size()
df4 = df.groupby(df['prediction_model']).size()
df2_sorted = df2.sort_index(ascending=True)
df4_sorted = df4.sort_index(ascending=True)
plt.plot(df4_sorted.index, df4_sorted, 'ro-', label = 'request user')
plt.bar(df2_sorted.index, df2_sorted, color='#ebf301', label = 'prediction user')
plt.title('Request by User and Prediction User')
plt.xlabel('Request and Prediction User')
plt.ylabel('Number Of Requests')
plt.xticks(rotation=45, ha='right')  # X축 레이블 회전 (텍스트가 길 경우) # ha = 'right' 레이블이 오른쪽정렬
plt.legend()

# 그래프 출력
st.pyplot(plt)
