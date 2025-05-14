from openai import OpenAI
from dotenv import load_dotenv
import os

# ─────────────────────────────────────
# 환경 설정 - API 키 로딩
# ─────────────────────────────────────
load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# ─────────────────────────────────────
# 모델 및 클라이언트 설정
# ─────────────────────────────────────
client = OpenAI()
MODEL_IMG = "gpt-image-1"           #dall-e-3, GPT-4o 수준의 LLM 해석+이미지 생성, ~$0.04–$0.08/장, 기관인증 필요
MODEL_IMG_LOWCOST = "dall-e-2"      #저비용, ~$0.016/장

# ─────────────────────────────────────
# 이미지 프롬프트 정의
# ─────────────────────────────────────
PROMPT = """
A warm and cheerful illustration of a baby hugging a stuffed bunny, 
surrounded by soft flowers and pastel colors, in a gentle children's book style.
"""

# ─────────────────────────────────────
# 이미지 생성 요청
# ─────────────────────────────────────
result = client.images.generate(
    # model = MODEL_IMG_LOWCOST,
    model = MODEL_IMG,
    prompt = PROMPT,
    # size="256x256", #저렴한 해상도
    size="1024x1024", #높은 해상도
    n=1             #1장 생성
)

#-----------------
# 결과 출력
#-----------------
image_url = result.data[0].url
print("Image URL:", image_url)