import os
from dotenv import load_dotenv
from openai import OpenAI

# ─────────────────────────────────────────────
# 환경 변수에서 OpenAI API 키 로드
# ─────────────────────────────────────────────
load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# ─────────────────────────────────────────────
# OpenAI 클라이언트 인스턴스 생성
# ─────────────────────────────────────────────
client = OpenAI()

# ─────────────────────────────────────────────
# 모델 설정
# ─────────────────────────────────────────────
MODEL_S ="gpt-4.1-nano-2025-04-14"
MODEL_M = "gpt-4.1"
MODEL_4o = "gpt-4o-mini"

# ─────────────────────────────────────────────
# 스토리 생성 요청
# ─────────────────────────────────────────────
response = client.responses.create(
    model = MODEL_S,
    input= [
    {
        "role": "user", 
        "content": "Write a one-sentence summary of HarryPotter book 1 story."}
    ]
)

# ─────────────────────────────────────────────
# 실행 "output_text"로 편리하게 출력. Completion과 Response는 다름
# pip show openai : Version: 1.81.0  (1.22.0 이상에서만 responses 사용 가능)
# ─────────────────────────────────────────────
print(response.output_text)
