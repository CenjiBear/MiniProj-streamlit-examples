# taken from: https://docs.streamlit.io/library/get-started/create-an-app

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

import datetime
from datetime import date
today = date.today()
st.write("# Today's date is ", today)

st.write('# Avocado Prices dashboard')  #st.title('Avocado Prices dashboard')
st.markdown('''
This is a dashboard showing the *average prices* of different types of :avocado:  
Data source: [Kaggle](https://www.kaggle.com/datasets/timmate/avocado-prices-2020)
''')
st.header('Summary statistics')
st.header('Line chart by geographies')

st.header('Summary statistics')
avocado = pd.read_csv('hello_world/avocado.csv')
# avocado_stats = avocado.groupby('type')['average_price'].mean()
# st.dataframe(avocado_stats)

st.markdown('''
We encounter difficulties with loading the data ... to show the dashboard.
''')