import os
from dotenv import load_dotenv
from openai import OpenAI

# ─────────────────────────────────────────────
# 환경 변수에서 OpenAI API 키 로드
# ─────────────────────────────────────────────
load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")
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
    input="Write a one-sentence summary of HarryPotter book 1 story."
)

# ─────────────────────────────────────────────
# 실행
# ─────────────────────────────────────────────
print(response.output_text)

# print(response["output"][0]["role"])
# print(response["output"][0]["content"][0]["text"])
# print(response["usage"]["total_tokens"])

print(f'model_dump_json: {response.output[0].content[0].model_dump_json()}')
print(f'model_json_schema: {response.output[0].content[0].model_json_schema()}')
print(f'model_dump: {response.output[0].content[0].model_dump()}')
print(f'text: {response.output[0].content[0].text}')