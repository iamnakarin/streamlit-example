
from sklearn import tree
import streamlit as st
import pandas as pd
model = tree.DecisionTreeClassifier()
url1=st.file_uploader("https://apps.samsenwit.ac.th/vichakarn/file/data.csv", type={"csv", "txt"})
feature=pd.read_csv(url1)
url2=st.file_uploader("ttps://apps.samsenwit.ac.th/vichakarn/file/label.csvv", type={"csv", "txt"})
label =pd.read_csv(url2)
#txt1=st.number_input('Enter a number1')
#txt2=st.number_input('Enter a number2')
#txt3=st.number_input('Enter a number3')
#model.fit(feature,label)
#st.write(model.predict([[txt1,txt2,txt3]]))
st.write(label)
