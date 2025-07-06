#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
from fuzzywuzzy import process, fuzz
import streamlit as st

# Load dữ liệu
df = pd.read_excel(r"F:\1.MSC\CREATE PAGE\CHATBOT\CHATBOT RULE BASE\300 skin care question.xlsx")
df.columns = df.columns.str.strip().str.lower()
questions = df['question'].tolist()

# Hàm xử lý
def get_answer(user_question):
    best_match, score = process.extractOne(user_question, questions, scorer=fuzz.WRatio)

    if score >= 50:
        answer = df[df['question'] == best_match]['answer'].values[0]
        return answer
    else:
        return "❓ Xin lỗi, tôi chưa hiểu câu hỏi. Bạn có thể hỏi cách khác được không?"

# Giao diện mới: hỗ trợ chat nhiều lượt
st.set_page_config(page_title="Chatbot Fuzzy", page_icon="👩‍⚕️")
st.title("👩‍⚕️ Chatbot Rule-based (Fuzzy Matching)")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Hiển thị lịch sử chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Hộp nhập câu hỏi
if prompt := st.chat_input("Bạn hãy nhập câu hỏi..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    answer = get_answer(prompt)
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)


# In[ ]:





# In[ ]:




