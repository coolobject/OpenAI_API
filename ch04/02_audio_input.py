import os
from dotenv import load_dotenv
from openai import OpenAI

# ─────────────────────────────────────────────
# 환경 변수에서 OpenAI API Key 로딩
# ─────────────────────────────────────────────
load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

# ─────────────────────────────────────────────
# 모델 설정
# ─────────────────────────────────────────────
MODEL = "whisper-1"  # 음성번역

# ─────────────────────────────────────────────
# 음성번역 모델 whisper-1
# ─────────────────────────────────────────────
audio_file = open("D:\work\KPC_OpenAI_Gpt_API\openai_d1\chat_dog.wav", "rb")

translation = client.audio.translations.create(
    model=MODEL, 
    file=audio_file,
)

print(translation.text)