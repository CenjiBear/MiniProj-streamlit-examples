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

# DATA_URL = ('https://www.kaggle.com/datasets/neuromusic/avocado-prices/download?datasetVersionNumber=1')

data = pd.read_csv('hello_world/avocado.csv')

# data = pd.read_csv(DATA_URL, nrows=1000)

st.header('Summary statistics')
# avocado = pd.read_csv('avocado-updated-2020.csv')
avocado = data
avocado_stats = avocado.groupby('type')['average_price'].mean()
st.dataframe(avocado_stats)

# abc