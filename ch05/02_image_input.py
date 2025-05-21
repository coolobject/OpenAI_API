import os
import base64
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
model_s="gpt-4-turbo"
model_m = "gpt-4.1"

# sample_img.png를 base64로 인코딩
with open("sample_img.png", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

# Data URL 형식으로 변환
image_data_url = f"data:image/png;base64,{encoded_image}"

response = client.responses.create(
  model = model_s,
  input = [
    {
      "role": "user",
      "content": [
        {
          "type": "input_image",
          "image_url": image_data_url
        },
        {
          "type": "input_text",
          "text": "이미지를 설명해줘."
        }
      ]
    }
  ],
  text={
    "format": {
      "type": "text"
    }
  },
  reasoning={},
  tools=[],
  temperature=1,
  max_output_tokens=512,
  top_p=1,
  store=True
)

print(response.output_text)