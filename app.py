from openai import OpenAI
import streamlit as st

f=open("E:\Flask\open-ai\genai_app_1\key.txt")
key=f.read()
client=OpenAI(api_key=key)
st.snow()
st.title(" Code Reviewer")
st.subheader("Write your python code")

prompt=st.text_input(" please provide the code")

if st.button("review") == True:
    st.balloons()


    response=client.chat.completions.create(
             model="gpt-3.5-turbo-0301",
             messages=[ 
            {"role":"system","content":"""You are a helpful AI Assistant and Code reviewer
            Find the Bugs and error and display corrected clean code ."""},
            {"role":"user","content":prompt}
            ] 
    )
    
    st.write(response.choices[0].message.content)