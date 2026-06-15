import streamlit as st
from ollama_chain import generate_response

st.title("Langchain + Ollama Chatbot")

if "chat_history" not in st.session_state:
   st.session_state.chat_history = []

prompt = st.text_input("You:")
if st.button("Send") or prompt:
   response = generate_response(prompt)
   st.session_state.chat_history.append(("You",
prompt))
   st.session_state.chat_history.append(("Bot",
response))
   
for speaker,msg in st.session_state.chat_history:
   st.chat_message("user" if speaker == "You"else
"assistant").write(msg)