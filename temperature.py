from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI(model='')
import streamlit as st

st.header("Reaserch Tool")
user_input=st.text_input('ENter your promopt')
if st.button('summaries'):
    result=model.invoke(user_input)
    st.write(result.content)