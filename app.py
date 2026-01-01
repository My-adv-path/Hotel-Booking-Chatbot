import streamlit as st
import os
from google.cloud import dialogflow_v2 as dialogflow

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="homeaway-inn-chatbot.json"
project_ID = "homeaway-inn-chatbot-jy9a"

def detect_intent(text,session_id):
    client=dialogflow.SessionsClient()
    session=client.session_path(project_ID,session_id)
    text_input=dialogflow.TextInput(text=text,language_code="en-US")
    query_input=dialogflow.QueryInput(text=text_input)
    response=client.detect_intent(request={"session":session,"query_input":query_input})
    return response.query_result.fulfillment_text

st.set_page_config(page_title="HOMEAWAY_inn")
st.title("HOMEAWAY_INN CHATBOT")

if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

user_input=st.text_input("you:")

if user_input:
    bot_reply=detect_intent(user_input,"session-01")
    st.session_state.chat_history.append(("You",user_input))
    st.session_state.chat_history.append(("Bot",bot_reply))

for sender,message in st.session_state.chat_history:
    st.write(f"**{sender}:**,{message}")
