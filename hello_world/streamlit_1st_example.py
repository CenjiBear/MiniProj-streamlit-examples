# taken from: https://docs.streamlit.io/library/get-started/create-an-app

import streamlit as st
import pandas as pd
import numpy as np

st.write('# Avocado Prices dashboard')  #st.title('Avocado Prices dashboard')
st.markdown('''
This is a dashboard showing the *average prices* of different types of :avocado:  
Data source: [Kaggle](https://www.kaggle.com/datasets/timmate/avocado-prices-2020)
''')
st.header('Summary statistics')
st.header('Line chart by geographies')
