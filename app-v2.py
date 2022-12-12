# >  streamlit run app.py
# import requirements, 加入函式庫
import streamlit as st
import joblib
import pandas as pd
from pycaret.regression import load_model, predict_model
# load the model, 載入模型
model = load_model('2022_12_8_cat_reg')
# acclaimed the purpose of this app, 陳述應用程式的目的

st.title('男或女？')
st.markdown("## 請輸入你的身高 (cm), 體重(kg) ")
st.subheader('然後讓我猜測你的性別')
# options for input,製造輸入選項
weight = st.slider('體重',min_value=40, max_value=100, value=50,step=1)
height = st.slider('身高',min_value=140, max_value=200, value=160,step=1)

features = [height,weight]
# guesss if clicked, 開始預測
if st.button('Predict'):
    #input_data=pd.DataFrame({'Height':[height],'Weight':[weight]})
    #model=joblib.load("2022_12_8_reg.pkl")i
    BMI=weight/weight**2*10000
    input_data=pd.DataFrame({'Height':[height],'Weight':[weight],'BMI':[BMI]})
    prediction = model.predict(input_data)
    result = model.predict(input_data)[0]
    # convert to classification, 將資料轉為類別
    if result<=0.5:
       gender='女'
    else:
       gender='男' 
    # print out the output, 結果
    st.success(f'讓我猜猜: {gender}')
