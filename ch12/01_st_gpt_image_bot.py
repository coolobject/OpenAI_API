import base64
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# ─────────────────────────────────────────────
# 환경 변수에서 OpenAI API 키 로드
# ─────────────────────────────────────────────
load_dotenv()
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ─────────────────────────────────────────────
# OpenAI 클라이언트 인스턴스 생성
# ─────────────────────────────────────────────
client = OpenAI()

# 타이틀 표시
st.title("🧠 ChatGPT-like Clone with Image Upload (GPT-4o)")

# 모델 고정
MODEL = "gpt-4o"

# 채팅 이력 초기화 (텍스트만 저장)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 이미지 업로드
uploaded_image = st.file_uploader("이미지를 업로드하세요 (선택)", type=["png", "jpg", "jpeg"])

# 이전 채팅 출력
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력
if prompt := st.chat_input("메시지를 입력하세요..."):
    # 세션에 텍스트만 저장 (UI 출력용)
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })
    # 사용자 메시지 출력
    with st.chat_message("user"):
        st.markdown(prompt)
        if uploaded_image:
            st.image(uploaded_image, caption="업로드한 이미지", use_container_width=True)    

    # OpenAI에 보낼 메시지 구성
    openai_messages = []
    for m in st.session_state.messages:
        openai_messages.append({
            "role": m["role"],
            "content": m["content"]
        })

    # 마지막 메시지에 이미지 포함 시 vision 포맷으로 덮어쓰기
    if uploaded_image:
        image_bytes = uploaded_image.read()
        encoded_image = base64.b64encode(image_bytes).decode()
        mime_type = uploaded_image.type
        openai_messages[-1]["content"] = [
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {
                "url": f"data:{mime_type};base64,{encoded_image}"
            }}
        ]        

    # 어시스턴트 응답 출력
    with st.chat_message("assistant"):
        try:
            stream = client.chat.completions.create(
                model=MODEL,
                messages=openai_messages,
                stream=True
            )
            response = st.write_stream(stream)
        except Exception as e:
            st.error(f"❌ 에러 발생: {e}")
            response = "⚠️ 오류가 발생했어요."            

    # 어시스턴트 메시지 저장
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })            