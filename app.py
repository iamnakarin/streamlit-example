
from sklearn import tree
import streamlit as st
import pandas as pd
model = tree.DecisionTreeClassifier()
feature =pd.read_csv('https://apps.samsenwit.ac.th/vichakarn/file/data.csv')
label =pd.read_csv('https://apps.samsenwit.ac.th/vichakarn/file/label.csv')
txt1=st.number_input('Enter a number1')
txt2=st.number_input('Enter a number2')
txt3=st.number_input('Enter a number3')
model.fit(feature,label)
st.write(model.predict([[txt1,txt2,txt3]]))
