import streamlit as st
from langchain_community.llms import Ollama

st.set_page_config(page_title="Local ChatBot")
st.title("Local Chatbot with gemma3")

llm = Ollama (model="gemma3")
user_input = st.text_input("Enter your message:")

if st.button("Send") or user_input:
    if user_input.strip():
        with st.spinner("Thinking..."):
            response = llm.invoke(user_input)
            st.markdown(f"LLM Bot: {response}")
    else:
        st.warning("Please enter a prompt.")
        