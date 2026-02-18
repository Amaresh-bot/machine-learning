import streamlit as st
st.title("Streamlit Text Input")

name=st.text_input("Please enter your name")

age = st.slider('select your age',1,100,15)
st.write("Your age is",age)

options = ['Biryani','Pizza','Pasta','Burger']
food = st.selectbox("Select your favourite food",options)
st.write("Your favourite food is",food)

if name:
    st.write("Hello",name)


upload = st.file_uploader("Choose a CSV file",type='csv')