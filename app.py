
from sklearn import tree
import streamlit as st
import pandas as pd
model = tree.DecisionTreeClassifier()
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  feature = pd.read_csv(uploaded_file)
  st.write(feature)
            
uploaded_file2 = st.file_uploader("Choose a file")
if uploaded_file2 is not None:
  label = pd.read_csv(uploaded_file2)
  st.write(label)



txt1=st.number_input('Enter a number1')
txt2=st.number_input('Enter a number2')
txt3=st.number_input('Enter a number3')
model.fit(feature,label)
st.write(model.predict([[txt1,txt2,txt3]]))
