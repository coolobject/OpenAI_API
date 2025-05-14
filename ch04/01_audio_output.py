import os
import base64
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
MODEL_CHAT = "gpt-4o-audio-preview"  # Chat 응답 + Audio
MODEL_TTS = "tts-1"                  # Text-to-Speech
VOICE_CHAT = "alloy"
VOICE_TTS = "fable"

# ─────────────────────────────────────────────
# GPT-4o 멀티모달 Chat 오디오 생성 함수
# ─────────────────────────────────────────────
def create_chat_audio(prompt_text: str, output_name="chatfile.wav"):
    print("Generating audio with GPT-4o...")

    completion = client.chat.completions.create(
        model=MODEL_CHAT,
        modalities=["text", "audio"],
        audio={"voice": VOICE_CHAT, "format": "wav"},
        messages=[{"role": "user", "content": prompt_text}]
    )

    wav_bytes = base64.b64decode(completion.choices[0].message.audio.data)
    output_path = os.path.join(os.getcwd(), output_name)
    
    with open(output_path, "wb") as f:
        f.write(wav_bytes)

    print(f"✅ GPT-4o Chat Audio saved to: {output_path}")

# ─────────────────────────────────────────────
# TTS 오디오 생성 함수
# ─────────────────────────────────────────────
def create_tts(prompt_text: str, output_name="ttsfile.wav"):
    print("Generating audio with tts-1...")

    response = client.audio.speech.create(
        model=MODEL_TTS,
        voice=VOICE_TTS,
        input=prompt_text,
        response_format="wav"
    )

    output_path = os.path.join(os.getcwd(), output_name)

    with open(output_path, "wb") as f:
        f.write(response.content)

    print(f"✅ TTS-1 Audio saved to: {output_path}")

# ─────────────────────────────────────────────
# 사용자 입력에 따라 실행
# ─────────────────────────────────────────────
def main():
    choice = input("Select mode:\n 1: GPT-4o Chat with audio\n 2: TTS with tts-1\n> ")
    PROMPT_TEXT = "Is a golden retriever a good family dog?"

    match choice:
        case "1":
            create_chat_audio(PROMPT_TEXT, output_name="sample.wav")
        case "2":
            create_tts(PROMPT_TEXT, output_name="sample.wav")
        case _:
            print("❌ Invalid selection. Please choose 1 or 2.")

if __name__ == "__main__":
    main()