import os
from typing import List
from dotenv import load_dotenv
from pydantic import BaseModel
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
# 텍스트 데이터 입력 
# ─────────────────────────────────────────────
FULL_TEXT = """
Harry Potter, a young boy raised by unkind relatives, discovers on his 11th birthday that he is a wizard. He attends Hogwarts School of Witchcraft and Wizardry where he makes new friends, learns magic, and uncovers the mystery of the Sorcerer’s Stone.
Harry, along with his friends Ron and Hermione, finds out that the Stone grants immortality. They suspect that someone at the school is trying to steal it. Eventually, they learn that Professor Quirrell, under the control of the dark wizard Voldemort, is attempting to take the Stone.
With courage and teamwork, the trio navigates magical obstacles to reach the Stone. Harry confronts Quirrell and Voldemort, and through his bravery, prevents them from getting the Stone. Dumbledore later explains that Harry was protected by his mother’s love.
In the end, Harry returns to the Dursleys for the summer, forever changed by his magical experiences and friendships.
"""

# ─────────────────────────────────────────────
# 출력 구조 정의 (Pydantic 사용)
# ─────────────────────────────────────────────
class StorySummary(BaseModel):
    title: str
    main_characters: List[str]
    setting: str
    conflict: str
    resolution: str
    themes: List[str]

# ─────────────────────────────────────────────
# 구조화 응답 요청 및 출력
# ─────────────────────────────────────────────
def extract_story_structure(text: str) -> StorySummary:
    response = client.responses.parse(
        model = MODEL_4o,
        input = [
            {
                "role": "system",
                "content": "You are an expert at structured data extraction. You will be given unstructured text and should convert it into the given structure.",
            },
            {"role": "user", "content": text},
        ],
        text_format = StorySummary,
    )
    return response.output_parsed

# ─────────────────────────────────────────────
# 실행
# ─────────────────────────────────────────────
if __name__ == "__main__":
    summary = extract_story_structure(FULL_TEXT)
    print(summary)
