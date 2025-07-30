# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 15:35:48 2025

@author: HP
"""

import pickle
import streamlit as st
import pandas as pd
df1=pickle.load(open("D:/concrete/pt.pkl",'rb'))
df=pickle.load(open("D:/concrete/model5.pkl",'rb'))
st.title("Concreter Strength Prediction")
Cement=st.number_input("Enter the cement")
Blast_Furnace_Slag=st.number_input("Enter the amount")
Fly_Ash=st.number_input("Enter the fly ash amount")
Water=st.number_input("Enter the water amount")
Superplasticizer=st.number_input("Superplasticizert")
Coarse_Aggregate=st.number_input("Coarse_Aggregate")
Fine_Aggregate=st.number_input("Fine_Aggregate")
Age=st.number_input("Age")
if st.button("Predict Strength"):
    b=df1.transform([[Cement,Blast_Furnace_Slag,Fly_Ash,Water,Superplasticizer,Coarse_Aggregate,Fine_Aggregate,Age]])
    a=df.predict(b)
    st.success(a)