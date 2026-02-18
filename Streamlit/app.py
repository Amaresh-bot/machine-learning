import streamlit as st
import pandas as pd
import numpy as numpy

##title of the application
st.title("My first Streamlit Application")

##Display simple text
st.text("Hi, I am Amaresh studying Machine Learning")

##Display Dataframe
df = pd.DataFrame({
    'Food' : ['Biryani','Pizza','Pasta','Burger'],
    'Price' : [250,300,150,200]
})

##displaying dataframe
st.write('Here is the food menu')
st.write(df)

##Create line chart
st.line_chart(df['Price'])