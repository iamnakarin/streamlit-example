import streamlit as st
import numpy as np
import pandas as pd
st.title('Basic Streamlit by Uncle Engineer')
st.write("ลุงจะมาสอน Python Visualization ด้วย Streamlit เร็วๆนี้")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)
