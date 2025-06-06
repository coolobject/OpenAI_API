import base64
import streamlit as st
from openai import OpenAI

# 페이지 설정
st.set_page_config(page_title="🧠 멀티모달 챗봇", page_icon="🤖")
st.title("🧠 OpenAI 멀티모달 챗봇")
st.markdown("텍스트, PDF, 이미지 입력을 받아 응답하는 GPT-4o 기반 챗봇")

# ─────────────────────────────────────────────
# API_KEY 설정 방법
# ─────────────────────────────────────────────
# 1) 환경 변수에서 OpenAI API 키 로드
# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

with st.sidebar:
    # 2) 직접 화면에서 API 키 입력
    input_api_key = st.text_input(label='API Key 입력', type ='password')

# API 키가 입력되지 않은 경우 경고 메시지 표시
if not input_api_key:
    st.warning("API 키를 입력해주세요.")

# 사이드바
with st.sidebar:
    selected_model = st.radio(
        "Choose a GPT ",
        ("gpt-3.5-turbo", "gpt-4", "gpt-4o-mini")
    )
    st.write(f"선택한 모델: {selected_model}")


with st.sidebar:
    selected_temperature = st.radio(
        "Temperture",
        (0.2, 0.4, 1.0, 1.2, 1.5)
    )
    st.write(f"선택한 온도: {selected_temperature}")

# ─────────────────────────────────────────────
# OpenAI 클라이언트 인스턴스 생성
# ─────────────────────────────────────────────
client = OpenAI(api_key=input_api_key)
    

# 메시지 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "당신은 친절하고 유능한 비서입니다. 파일이나 이미지를 분석하고 텍스트 기반 질문에 답변하세요."}
    ]

# 기존 메시지 출력
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 파일 업로드
uploaded_file = st.file_uploader("📎 파일을 첨부하세요 (PDF 또는 이미지)", type=["pdf", "png", "jpg", "jpeg"])

# 사용자 입력
user_input = st.chat_input("메시지를 입력하세요...")

if user_input:
    # 사용자 메시지 표시
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    file_block = []
    if uploaded_file:
        mime_type = uploaded_file.type
        file_bytes = uploaded_file.read()
        encoded = base64.b64encode(file_bytes).decode("utf-8")

        if "pdf" in mime_type:
            file_block.append({
                "type": "input_file",
                "filename": uploaded_file.name,
                "file_data": f"data:application/pdf;base64,{encoded}"
            })
        elif "image" in mime_type:
            file_block.append({
                "type": "input_image",
                "image_url": f"data:{mime_type};base64,{encoded}"
            })

    # GPT 응답 생성
    response = client.responses.create(
        model=selected_model,
        temperature=selected_temperature,
        input=[
            {
                "role": "user",
                "content": file_block + [{"type": "input_text", "text": user_input}]
            }
        ]
    )

    assistant_reply = response.output_text.strip()

    with st.chat_message("assistant"):
        st.markdown(assistant_reply)

    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
