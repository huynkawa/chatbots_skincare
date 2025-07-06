import openai
import streamlit as st

# Cài key OpenAI API của bạn tại đây
openai.api_key = st.secrets["openai_api_key"]  # ✅ an toàn


st.set_page_config(page_title="💬 GPT-4 Skincare Chatbot", page_icon="💬")
st.title("💬 GPT-4 Skincare Chatbot")
st.subheader("Tư vấn chăm sóc da với trí tuệ nhân tạo 🤖")

# Giao diện nhập câu hỏi
user_input = st.text_input("Bạn hãy nhập câu hỏi về chăm sóc da:")

# Hàm gọi GPT
def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",   # hoặc gpt-3.5-turbo nếu bạn không có quyền dùng gpt-4
        messages=[
            {"role": "system", "content": "Bạn là chuyên gia chăm sóc da. Hãy trả lời ngắn gọn, dễ hiểu."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

# Hiển thị câu trả lời
if user_input:
    with st.spinner("Đang trả lời..."):
        answer = ask_gpt(user_input)
        st.success(answer)
