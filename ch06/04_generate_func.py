import os
from dotenv import load_dotenv
from openai import OpenAI

# ─────────────────────────────────────────────
# 환경 변수에서 OpenAI API 키 로드
# ─────────────────────────────────────────────
load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# ─────────────────────────────────────────────
# 모델 설정
# ─────────────────────────────────────────────
MODEL_S = "gpt-3.5-turbo"
MODEL_M = "gpt-4.1"
MODEL_4o = "gpt-4o-mini"

# ─────────────────────────────────────────────
# OpenAI 클라이언트 인스턴스 생성
# ─────────────────────────────────────────────
client = OpenAI()

# 프롬프트 템플릿 생성
def interview_prompt_template(question: str, answer: str) -> str:
    return (
        f"면접관: {question}\n"
        f"지원자: {answer}\n"
        "지원자의 답변에 대해 논리성 및 구체성을 간단히 평가 후, 다음 면접관 질문을 해주세요."
    )

# GPT 모델 설정, 클라이언트 생성 
def call_gpt(prompt: str, model: str, temperature: float) -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature
    )
    return response.choices[0].message.content

# main 호출
if __name__ == "__main__":
    question = "OpenAI API 사용 경험이 있나요? (종료하려면 'exit' 입력) "
    ans = input(f"{question}")
    
    if ans.lower() == "exit":
        print("종료합니다.")
        exit()

    prompt = interview_prompt_template(question, ans)
    print(call_gpt(prompt, MODEL_S, 0.7))