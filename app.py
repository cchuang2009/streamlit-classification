# >  streamlit run app.py
# ToDo: model predict not completed

import streamlit as st

import pandas as pd

from pycaret.classification import load_model, predict_model

st.title('男或女？')

model = load_model('2022_12_8')

st.markdown("## 請輸入你的身高 (cm), 體重(kg) ")
st.subheader('然後讓我猜測你的性別')

weight = st.slider('體重',min_value=40, max_value=100, value=50,step=1)
height = st.slider('身高',min_value=140, max_value=200, value=160,step=1)

features = [height,weight]
#final_features = np.array(features).reshape(1, -1)

if st.button('Predict'):
    input_data=pd.DataFrame({'身高':[height],'體重':[weight]})
    #result = model.predict(final_features)
    result=prediction=predict_model(model,data=input_data)['prediction_label'][0]
    if result==0:
       gender='女'
    else:
       gender='男' 

    st.success(f'讓我猜猜: {gender}')
