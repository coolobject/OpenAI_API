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
model_s="gpt-4.1-nano-2025-04-14"
model_m = "gpt-4.1"

response = client.responses.create(
    model=model_s,
    input=[
        {
            "role": "user",
            "content": "이미지에 있는 캐릭터들의 이름은?"
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "input_image",
                     "image_url": "https://static.ebs.co.kr/images/bhp/public/images/2023/08/25/15/39/21/dd6f4773-874b-42ee-9db7-9ba8fa4b91da.jpg"
                }
            ]
        }
    ]
)

print(response.output_text)