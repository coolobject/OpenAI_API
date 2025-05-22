import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

# 환경 변수 로드
load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": """
            당신은 인터뷰 시뮬레이터입니다. User는 '지원자' 역할로 답변합니다.
            당신은 응답 시 다음 형식을 반드시 따릅니다:

            (모범답안 →) (지원자의 답변을 바탕으로 한 이상적인 답변 예시 100~150자)
            면접관: (다음 질문)
            지원자:
            """
        }
    ]

# 타이틀 및 안내
st.title("👨‍🦰👩‍🦰 AI 면접 코치")
st.write("아래에 답변을 입력하면 GPT가 모범답안과 다음 질문을 제시합니다.\n 자기소개로 시작하세요.")

# 입력 폼
with st.form("interview_form"):
    user_input = st.text_area("지원자:", height=100)
    submitted = st.form_submit_button("제출")

if submitted and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("면접관이 생각 중입니다..."):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=st.session_state.messages,
            temperature=0.7,
            max_tokens=600,
            stop=["지원자:"],
            top_p=1
        )

    reply = response.choices[0].message.content.strip()
    st.session_state.messages.append({"role": "assistant", "content": reply})

# 대화 출력
for message in st.session_state.messages[1:]:
    if message["role"] == "user":
        st.markdown(f"**지원자:** {message['content']}")
    elif message["role"] == "assistant":
        st.markdown(f"**면접관:** {message['content']}")
