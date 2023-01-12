

from streamlit_option_menu import option_menu
from xgboost import XGBRegressor
import pandas as pd
import numpy as np 
import streamlit as st
import build_model
import experiment
import ml_model
import theory



with st.sidebar:
    selected = option_menu(
        menu_title='Iron Ore Purity',
        options=['Theory',
                 'Experiment',
                 'Model Building',
                 'Model Prediction'],
        icons=['book-half',
               'clipboard-data',
               'gear',
               'cpu'],
        default_index=0,
        menu_icon=['app-indicator'],
        )
    
st.sidebar.title('Made with \u2764\ufe0f by RSK')

if selected == 'Theory':
    theory.Theory()
    
elif selected == 'Experiment':
    experiment.Experiment()

elif selected == 'Model Building':
    build_model.buildModel()
    
elif selected == 'Model Prediction':
    ml_model.ML_Model()



    










