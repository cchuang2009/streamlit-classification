[streamlit-classification, Deployment](https://github.com/cchuang2009/streamlit-classification)
---
This is a simple streamlit app for surpervised model: Gender Guess. The model was made by the 
- [code]( https://github.com/cchuang2009/2022-1/blob/main/Python_IM/Week12_Gender_Predition_colab.ipynb)
 and deployed directly on [streamlit official site](http://share.streamlit.io).

This app was made by less-code AotoML Pycaret. Though guessing is a classical surpervized learning, this app, **app-v2.py**, was created by regression model but not classification model, due to the the confliction between pycaret.classification and scikit-learn. 

Note
---
Last conclusion is not right, the deployment can not be run because of "decision-trrr" not worked but "catboost" does!
Run catboost deploy by the following:
```
> streamlit run app-v2.py
```
