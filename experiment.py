

import streamlit as st
import pandas as pd
import numpy as np

resultData = pd.read_csv('expResult.csv').iloc[:,1:]

aim = '''To measure the quality of obtained ore concentrate from froth floatation
column by adjusting the pulp quality and other floatation column parameters.'''

paramUsed = '''1. % Iron 
2. Starch Flow
3. Amina Flow
4. Ore Pulp Flow
5. Ore Pulp pH
6. Ore Pulp Density
7. Flotation Column Air Flow
8. Flotation Column Level
9. % Iron Concentrate'''

procedure = '''
1. Crush the ore into very fine powder-paricles to increase its surface area
2. Mix this powdered form if ore with water. The obtained mixture is called 'Slurry'.
3. Add collector which will act as surfactant chemical. which will increase hydrophobicity of mineral.
4. After adding surfactant slurry is called 'Pulp'.
5. This pulp is then added into first floatation column filled with water.
6. Then air jets are forced into it to create bubbles.
7. Because of Hydrophobicity the required mineral is repelled by water and thus gets attached to air bubbles.
8. As these air bubbles rise up to the surface with mineral particles sticking to them, these are called 'froth'.
9. This Froth is sepearated and further taken for process of extraction.
'''

results = 'Add dataframe here.'

def Experiment():
    st.header('Aim')
    st.write(aim)
    st.header('Parameters Measured')
    st.write(paramUsed)
    st.header('Procedure')
    st.write(procedure)
    st.header('Results')
    st.write(resultData)
    







