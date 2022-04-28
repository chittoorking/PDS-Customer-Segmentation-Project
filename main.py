import base64
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import pickle

st.set_page_config(
    page_title="Customer Segmentation",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown(
    """
    <style>
        .css-hby737, .css-17eq0hr, .css-qbe2hs {
            background-color:    #154360    !important;
            color: black !important;
        }
        div[role="radiogroup"] {
            color:black !important;
            margin-left:8%;
        }
        div[data-baseweb="select"] > div {
            
            color: black;
        }
        div[data-baseweb="base-input"] > div {
            background-color: #aab7b8 !important;
            color: black;
        }
        
        .st-cb, .st-bq, .st-aj, .st-c0{
            color: black !important;
        }
        .st-bs, .st-ez, .st-eq, .st-ep, .st-bd, .st-e2, .st-ea, .st-g9, .st-g8, .st-dh, .st-c0 {
            color: black !important;
        }
        .st-fg, .st-fi {
            background-color: #c6703b !important;
            color: black !important;
        }
        
        .st-g0 {
            border-bottom-color: #c6703b !important;
        }
        .st-fz {
            border-top-color: #c6703b !important;
        }
        .st-fy {
            border-right-color: #c6703b !important;
        }
        .st-fx {
            border-left-color: #c6703b !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)


st.sidebar.markdown('<h1 style="margin-left:8%; color:#FA8072">Customer Segment Prediction</h1>', unsafe_allow_html=True)

add_selectbox = st.sidebar.radio(
    "",
    ("About", "Customer Segment Prediction", "Team")
)

#def pima():
if add_selectbox == 'About':
    
    st.subheader('ABOUT THE PROJECT')

    st.markdown('<h4>Background</h4>', unsafe_allow_html=True)
    st.markdown('''Owning any business involves some basic data about customers like name, age,
customer ID, amount spent etc. Understanding and planning a strategy on the cus-
tomers and targeting the marketing towards the buyers not only helps the business
grow faster but also leads to customer satisfaction''',unsafe_allow_html=True)
    
elif add_selectbox == 'Customer Segment Prediction':
	
      st.subheader('PREDICTION')
      pickle_in = open('KMeans_customer_deployed', 'rb')
      clusterer = pickle.load(pickle_in)

      st.markdown("## Customer Segment prediction ")
    
      name = st.text_input("Name:")
      Gender = st.number_input("Enter the Gender : 0:Female ,1:Male", min_value=0, max_value=1, step=1)
      Age = st.number_input("Enter Age ", min_value=1, max_value=100, step=1)
      Annual_income         =  st.number_input("Enter Annual Income in k$:", min_value=0, max_value=1000, step=1)
      spending_score    = st.number_input("Enter the spending_score", min_value=1, max_value=100, step=1)
      submit = st.button('Predict')

      if submit:
            prediction = clusterer.predict([[Gender,Age,Annual_income,spending_score]])
            st.write('Hi',name,'The predicted customer segment is',int(prediction))
elif add_selectbox == 'Team':
    
    st.subheader('Teamates')

    st.markdown('• <a href="https://www.linkedin.com/in/vamsi-chittoor-331b80189/">Chittoor Vamsi</a>',
                unsafe_allow_html=True)
    st.markdown('• <a href="https://www.linkedin.com/in/skajal1309/">kajal Srivastava</a>',
                unsafe_allow_html=True)
