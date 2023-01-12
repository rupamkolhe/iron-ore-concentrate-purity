
from xgboost import XGBRegressor
import streamlit as st
import numpy as np
import pickle 
import sklearn

global model 
with open('iron_concentrate','rb') as file:
    model = pickle.load(file)

def ML_Model():
    global model
    col1, col2, col3, col4 = st.columns([1,1,1,1])
    with col1:
        a = st.number_input('% Iron Feed',min_value=5.0,max_value=95.0,step=1.0,value=56.29)
        e = st.number_input('Ore Pulp pH',min_value=8.0,max_value=10.0,step=0.01,value=9.76)
        i = st.number_input('FC3 Air Flow',min_value=176.0,max_value=364.0,step=1.0,value=281.08)
        m = st.number_input('FC7 Air Flow',min_value=185.0,max_value=371.0,step=1.0,value=290.75)
        q = st.number_input('FC4 Level',min_value=162.0,max_value=680.0,step=2.0,value=420.32)
        
            
    with col2:
        b = st.number_input('Starch Flow',min_value=1.0,max_value=5000.0,step=2.0,value=2869.14)
        f = st.number_input('Ore Pulp Density',min_value=1.40,max_value=1.90,step=0.01,value=1.68)
        j = st.number_input('FC4 Air Flow',min_value=292.0,max_value=305.0,step=1.0,value=299.4)
        n = st.number_input('FC1 Level',min_value=149.0,max_value=862.0,step=2.0,value=520.24)
        r = st.number_input('FC5 Level',min_value=166.0,max_value=675.0,step=2.0,value=425.25)

    with col3:
        c = st.number_input('Amina Flow',min_value=240.0,max_value=700.0,step=2.0,value=488.14)
        g = st.number_input('FC1 Air Flow',min_value=175.0,max_value=373.0,step=1.0,value=280.15)
        k = st.number_input('FC5 Air Flow',min_value=286.0,max_value=310.0,step=0.5,value=299.9)
        o = st.number_input('FC2 Level',min_value=210.0,max_value=828.0,step=2.0,value=522.65)
        s = st.number_input('FC6 Level',min_value=155.0,max_value=698.0,step=2.0,value=429.94)
            
    with col4:
        d = st.number_input('Ore Pulp Flow',min_value=370.0,max_value=400.0,step=1.0,value=397.57)
        h = st.number_input('FC2 Air Flow',min_value=175.0,max_value=375.0,step=1.0,value=277.16)
        l = st.number_input('FC6 Air Flow',min_value=189.0,max_value=370.0,step=1.0,value=292.07)
        p = st.number_input('FC3 Level',min_value=126.0,max_value=886.0,step=2.0,value=531.35)
        t = st.number_input('FC7 Level',min_value=175.0,max_value=659.0,step=2.0,value=421.02)
    fVec = np.array([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t]).reshape(1,20)
    st.header("Expected Purity of Iron ore concentration :- "+str(round(model.predict(fVec)[0],2))+"%")
    
