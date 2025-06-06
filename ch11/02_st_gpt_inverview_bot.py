import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

# ─────────────────────────────────────────────
# 상수 및 시스템 프롬프트
# ─────────────────────────────────────────────
SYSTEM_PROMPT = (
    """
    당신은 인터뷰 시뮬레이터입니다. User는 '지원자' 역할로 답변합니다.
    당신은 응답 시 다음 형식을 반드시 따릅니다:

    (모범답안 →) (지원자의 답변을 바탕으로 한 이상적인 답변 예시 100~150자)  
    면접관: (다음 질문)
    지원자:
    """
)

# ─────────────────────────────────────────────
# 환경 변수 및 OpenAI 클라이언트 초기화
# ─────────────────────────────────────────────
def init_openai_client():
    load_dotenv()
    OpenAI.api_key = os.getenv("OPENAI_API_KEY")
    return OpenAI()

# ─────────────────────────────────────────────
# 세션 상태 초기화
# ─────────────────────────────────────────────
def init_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]

# ─────────────────────────────────────────────
# 사이드바 UI
# ─────────────────────────────────────────────
def sidebar_ui():
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
        st.write(f"선택한 온도도: {selected_temperature}")
    return selected_model, selected_temperature

# ─────────────────────────────────────────────
# 입력 폼 및 응답 처리
# ─────────────────────────────────────────────
def interview_form(client, selected_model, selected_temperature):
    with st.form("interview_form"):
        user_input = st.text_area("지원자:", height=150)
        submitted = st.form_submit_button("제출")

    if submitted and user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        user_input = ""
        with st.spinner("면접관이 생각 중입니다..."):
            response = client.chat.completions.create(
                model=selected_model,
                messages=st.session_state.messages,
                temperature=selected_temperature,
                max_tokens=600,
                stop=["지원자:"]
            )
        reply = response.choices[0].message.content.strip()
        st.session_state.messages.append({"role": "assistant", "content": reply})

# ─────────────────────────────────────────────
# 대화 출력
# ─────────────────────────────────────────────
def display_conversation():
    for message in st.session_state.messages[1:]:
        if message["role"] == "user":
            st.markdown(f"**지원자:** {message['content']}")
        elif message["role"] == "assistant":
            st.markdown(f"**면접관:** {message['content']}")

# ─────────────────────────────────────────────
# 메인 실행부
# ─────────────────────────────────────────────
def main():
    st.title("👨‍🦰👩‍🦰 AI 면접 코치")
    st.write("아래에 답변을 입력하면 GPT가 모범답안과 다음 질문을 제시합니다.\n 자기소개로 시작하세요.")
    client = init_openai_client()
    init_session_state()
    selected_model, selected_temperature = sidebar_ui()
    interview_form(client, selected_model, selected_temperature)
    display_conversation()

if __name__ == "__main__":
    main()
