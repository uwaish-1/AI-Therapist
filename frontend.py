# 1. SetUp Streamlit
import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000/ask"  # Replace with your backend URL

st.set_page_config(page_title="AI Mental Health Therapist", layout="wide")
st.title("SafeSpace - AI Mental Health Therapist")

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# 2. user is able to ask question
# Chat Input
user_input = st.chat_input("What's on your mind today?")
if user_input:
    # Append user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # AI agent exists here
    response = requests.post(BACKEND_URL, json={"message": user_input})

    st.session_state.chat_history.append({"role": "assistant", "content": f'{response.json()['response']} WITH TOOL: [{response.json()['tool_called']}]'})
# 3. Show response from backend

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
