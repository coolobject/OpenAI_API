import streamlit as st
import numpy as np

with st.chat_message("assistant"):
    st.write("Hello human")
    st.bar_chart(np.random.randn(30, 3))

with st.chat_message("user"):
    st.write("Hello 👋")    

# message = st.chat_message("assistant")
# message.write("Hello human")
# message.bar_chart(np.random.randn(30, 3))

# message = st.chat_message("user")
# message.write("Hello")

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")