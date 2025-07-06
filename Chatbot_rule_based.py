from openai import OpenAI  # Câu này nên đưa lên đầu file

client = OpenAI()  # Cũng đưa lên đầu file (chỉ cần tạo 1 lần)
import streamlit as st

def ask_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4",  # hoặc "gpt-3.5-turbo" nếu không có gpt-4
        messages=[
            {"role": "system", "content": "Bạn là chuyên gia chăm sóc da..."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


st.set_page_config(page_title="💬 GPT-4 Skincare Chatbot", page_icon="💬")
st.title("💬 GPT-4 Skincare Chatbot")
st.subheader("Tư vấn chăm sóc da với trí tuệ nhân tạo 🤖")

# Giao diện nhập câu hỏi
user_input = st.text_input("Bạn hãy nhập câu hỏi về chăm sóc da:")

# Hàm gọi GPT
def ask_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4",  # hoặc gpt-3.5-turbo nếu bạn không có quyền dùng gpt-4
        messages=[
            {"role": "system", "content": "Bạn là chuyên gia chăm sóc da. Hãy trả lời ngắn gọn, dễ hiểu."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Hiển thị câu trả lời
if user_input:
    with st.spinner("Đang trả lời..."):
        answer = ask_gpt(user_input)
        st.success(answer)
