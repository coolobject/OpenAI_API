import time
import os
from dotenv import load_dotenv
from openai import OpenAI

# 환경 변수에서 OpenAI API 키 로드
load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# OpenAI 클라이언트 인스턴스 생성 (1.78.0 버전 이상)
client = OpenAI()

# 1. Assistant 생성 (면접 연습 전용)
assistant = client.beta.assistants.create(
    name="면접 코치 GPT",
    instructions=(
        "당신은 사용자의 답변을 평가하고 다음을 제공합니다:\n"
        "1. STAR 기법 기반의 모범답안\n"
        "2. 척도 평가 (논리성, 구체성, 관련성: 각 5점 척도)\n"
        "3. 다음 면접 질문\n\n"
        "출력 형식은 다음과 같습니다:\n"
        "모범답안:\n...\n\n"
        "척도 평가:\n- 논리성: /5\n- 구체성: /5\n- 관련성: /5\n\n"
        "면접관: (다음 질문)"
    ),
    model="gpt-4o"
)

# 2. Thread 생성
thread = client.beta.threads.create()

# 3. 사용자 메시지 추가
user_input = (
    "면접관: 우리 회사에 지원하게 된 동기가 무엇인가요?\n"
    "지원자: 저는 유통 업계 데이터를 분석하며 실시간 대응의 중요성을 체감했고..."
)
client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=user_input
)

# 4. Run 실행
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
)

# 5. 응답 완료 대기
print("⏳ 면접 코치 GPT의 응답을 기다리는 중...")
while True:
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    if run_status.status == "completed":
        break
    elif run_status.status == "failed":
        raise RuntimeError("❌ Assistant 실행 실패")
    time.sleep(1)

# 6. Assistant 응답 출력
messages = client.beta.threads.messages.list(thread_id=thread.id)
assistant_reply = messages.data[0].content[0].text.value
print("\n📢 면접 코치 GPT의 응답:\n")
print(assistant_reply)
