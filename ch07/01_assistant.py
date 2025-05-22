import time
import os
from dotenv import load_dotenv
from openai import OpenAI

# 환경 변수에서 OpenAI API 키 로드
load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# OpenAI 클라이언트 인스턴스 생성
client = OpenAI()

messages=[
    {
    "role": "system",
    "content": """
            당신은 인터뷰 시뮬레이터입니다. User는 '지원자' 역할로 답변합니다. 
            당신은 응답 시 다음 형식을 반드시 따릅니다:
            
            (모범답안 →) (지원자의 답변을 바탕으로 한 이상적인 답변 예시 100자 이내)
            면접관: (다음 질문)
            지원자: 
            """
    }
]
print("⏳ 면접 코치 GPT입니다. 자기소개로 시작하세요. (종료하려면 'exit' 입력)")

while True:
    user_input = input("\n지원자: ")
    if user_input.lower() == "exit":
        print("면접 코치 GPT를 종료합니다.")
        break

    messages.append({"role": "user", "content": user_input})

    # OpenAI API 호출
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.7,
        max_completion_tokens=600,
        stop=["지원자:"],
        frequency_penalty=0.5,
        presence_penalty=0.5,
        store=False
    )

    reply = response.choices[0].message.content.strip() 
    print("\n면접관:", reply)

    # 다음 질문을 위해 메시지에 추가
    messages.append({"role": "assistant", "content": reply})

