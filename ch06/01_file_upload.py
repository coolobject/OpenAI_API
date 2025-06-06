# %%
import os
from dotenv import load_dotenv
from openai import OpenAI

# ─────────────────────────────────────────────
# 환경 변수에서 OpenAI API 키 로드
# ─────────────────────────────────────────────
load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")
# %%
client = OpenAI()
# %%
file = client.files.create(
    file=open("sample_file.pdf", "rb"),
    purpose="user_data"
)
#%%
file
# %%
response = client.responses.create(
    model="gpt-4.1",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_file",
                    "file_id": file.id,
                },
                {
                    "type": "input_text",
                    "text": "제일 중요한 단어 top 10 알려주세요, Please.",
                },
            ]
        }
    ]
)
# %%
print(response.output_text)