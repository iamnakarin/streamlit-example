
from sklearn import tree
import streamlit as st
import pandas as pd
model = tree.DecisionTreeClassifier()
feature =pd.read_csv('https://drive.google.com/file/d/1w5vSYGK2-hpZRyhnZGZmSJN3Kt5hylfD/view?usp=share_link')
label =pd.read_csv('https://drive.google.com/file/d/1-a_JQXsNJoyeYoo30P4YKNAljDWmPRn8/view?usp=share_link')
txt1=st.number_input('Enter a number1')
txt2=st.number_input('Enter a number2')
txt3=st.number_input('Enter a number3')
model.fit(feature,label)
st.write(model.predict([[txt1,txt2,txt3]]))
