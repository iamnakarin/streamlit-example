%%writefile app.py
import streamlit as st

import numpy as np
import pandas as pd

st.title('My first app')

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

st.sidebar.write(" I am a sidebar")
xx = st.sidebar.checkbox('sidebar checkbox')

if xx:
    st.sidebar.write('you checked a box!')
else:
    st.sidebar.write('Box is not checked')

text = st.text_area(
    "Your text",
    "I dreamed a dream."
)

if not text:
    text = "Emptiness"

st.write(text+" ---> auto add message")
