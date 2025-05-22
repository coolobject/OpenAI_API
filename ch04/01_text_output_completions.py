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
MODEL_S = "gpt-3.5-turbo"
MODEL_M = "gpt-4.1"
MODEL_4o = "gpt-4o-mini"

# ─────────────────────────────────────────────
# 스토리 생성 요청
# ─────────────────────────────────────────────

completion = client.chat.completions.create(
  model=MODEL_S,
  messages=[
      {
          "role": "user",
          "content": "Write a one-sentence summary of HarryPotter book 1 story."
      }
  ]
)

# ─────────────────────────────────────────────
# 실행 
# ─────────────────────────────────────────────
print(completion.choices[0].message.content)

# print(f'model_dump_json: {completion.choices[0].message.content[0].model_dump_json()}')
# print(f'model_json_schema: {completion.choices[0].message.content[0].model_json_schema()}')
# print(f'model_dump: {completion.choices[0].message.content[0].model_dump()}')
# print(f'text: {completion.choices[0].message.content[0].text}')