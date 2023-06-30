import streamlit as st
from mtranslate import translate
import pandas as pd
import os

# read language dataset from language excel file
df = pd.read_excel(os.path.join('data', 'language.xlsx'),sheet_name='wiki')
df.dropna(inplace=True)
lang = df['name'].to_list()
langlist=tuple(lang)
langcode = df['iso'].to_list()

# create dictionary of language and 2 letter langcode
lang_array = {lang[i]: langcode[i] for i in range(len(langcode))}

# layout
st.header("Welcome To My Language Translation App")
inputtext = st.text_area('Enter Text Here:',height=150)

st.sidebar.title("LANGUAGE")
st.sidebar.info("Select you preferred language here:")
choice = st.sidebar.radio('',langlist)
# I/O
if len(inputtext) > 0 :
    try:
        output = translate(inputtext,lang_array[choice])
        st.text_area("TRANSLATED TEXT",output,height=150)
        st.success("Done!")
        st.balloons()
    except Exception as e:
        st.error(e)
        st.error("enter a valid text")

st.image("img/Johnson.jpeg")
st.caption("Johnson Amodu")

st.markdown("Check out my github profile here (https://github.com/SolaJohnson/)")
st.markdown("Languages are pulled from language.xlsx dynamically !!")
