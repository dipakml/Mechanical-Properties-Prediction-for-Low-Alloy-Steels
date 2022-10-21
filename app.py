# -*- coding: utf-8 -*-
"""
Created on 

@author: DA
"""

# -*- coding: utf-8 -*-
"""

@Created by: DA
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image

pickle_in_ts = open("DecisionTree_TS.pkl","rb")
DecisionTree_TS = pickle.load(pickle_in_ts)  

pickle_in_el = open("XGBoost_el.pkl","rb")
XGBoost_el=pickle.load(pickle_in_el)  

pickle_in_ps = open("XGBoost_ps.pkl","rb")
XGBoost_ps =pickle.load(pickle_in_ps)  

pickle_in_ra = open("XGBoost_ra.pkl","rb")
XGBoost_ra =pickle.load(pickle_in_ra) 

pickle_in_ts_sc = open("sc_ts.pkl","rb")
sc_ts =pickle.load(pickle_in_ts_sc)  

pickle_in_el_sc = open("sc_el.pkl","rb")
sc_el=pickle.load(pickle_in_el_sc)  

pickle_in_ps_sc = open("sc_ps.pkl","rb")
sc_ps =pickle.load(pickle_in_ps_sc)  

pickle_in_ra_sc = open("sc_ra.pkl","rb")
sc_ra =pickle.load(pickle_in_ra_sc)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2017/12/03/20/31/background-2995826__480.png");

         }}
         
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 



def main():
    html_temp = """
    <div style="background-color:brown;padding:10px">
    <h1 style="color:white;text-align:center;">Prediction of Mechanical Properties of Low Alloy Steels </h1>
    </div>
    """
        
    st.markdown(html_temp,unsafe_allow_html=True)

    st.subheader('**This is a web application built using Machine Learning for prediction of mechanical properties of low alloy steels. Enter the chemical composition of steel, this web application will predict the mechanical properties.**')

    
    C = st.number_input("C")
    Si = st.number_input("Si")
    Mn = st.number_input("Mn")
    P = st.number_input("P")
    S = st.number_input("S")
    Ni = st.number_input("Ni")
    Cr = st.number_input("Cr")
    Mo= st.number_input("Mo")
    Cu= st.number_input("Cu")
    V = st.number_input("V")
    Al = st.number_input("Al")
    N = st.number_input("N")
    Ceq = st.number_input("Ceq")
    Nb_Ta = st.number_input("Nb_Ta")
    Temperature = st.number_input("Temperature")


    result=""

    if st.button('Predict 0.2% Proof Strength'):

        result = XGBoost_ps.predict(sc_ps.transform([[C,Si,Mn,P,S,Ni,Cr,Mo,Cu,V,Al,N,Ceq,Nb_Ta,Temperature]]))
        st.title("Predicted Proof strength is" +
             str(result)+"Mpa")

    result=""

    if st.button('Predict Tensile Strength'):

        result = DecisionTree_TS.predict(sc_ts.transform([[C,Si,Mn,P,S,Ni,Cr,Mo,Cu,V,Al,N,Ceq,Nb_Ta,Temperature]]))
        st.title("Predicted tensile strength is" +
             str(result)+"Mpa")

    result=""

    if st.button('Predict Elongation'):

        result = XGBoost_el.predict(sc_el.transform([[C,Si,Mn,P,S,Ni,Cr,Mo,Cu,V,Al,N,Ceq,Nb_Ta,Temperature]]))
        st.title("Predicted elongation is" +
             str(result)+"%")
  
    result=""

    if st.button('Predict Reduction in Area'):

        result = XGBoost_ra.predict(sc_ra.transform([[C,Si,Mn,P,S,Ni,Cr,Mo,Cu,V,Al,N,Ceq,Nb_Ta,Temperature]]))
        st.title("Predicted reduction in area is" +
             str(result)+"%")
  
  
if __name__=='__main__':
    main()
    
    
    