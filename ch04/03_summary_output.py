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
전 세계를 강타한 해리포터 시리즈가 다시 한번 화제를 일으키고 있다.  마법의 세계를 배경으로 한 해리포터 시리즈는 청소년을 중심으로 엄청난 인기를 끌고 있으며, 성인 독자들도 그 매력에 푹 빠져들었다.

해리포터는 고아이자 마법사인 주인공 해리의 성장과 모험을 다룬 소설로, 작가 J.K. 롤링의 뛰어난 상상력과 대단한 스토리텔링 능력으로 독자들을 매료시키고 있다. 해리포터가 겪는 어려움과 도전, 우정과 가족의 중 요성을 그리며, 독자들에게 용기와 희망을 전해주고 있는 것으로 평가받 고 있다.

해리포터 시리즈는 다양한 언어로 번역되어 전 세계적으로 사랑을 받고  있으며, 영화와 연극으로도 제작되어 팬들에게 더 많은 즐거움을 주고 있다. 또한 해리포터 주니어 시리즈 등을 통해 새로운 독자들에게도 사랑을 받고 있는 것으로 알려져 있다.

해리포터 시리즈는 7권의 소설로 완결되었지만, 여전히 많은 팬들로부터 사랑을 받고 있는 것으로 보아 영원한 명성을 가지고 있을 것으로 전망된사랑을 받고 있는 것으로 보아 영원한 명성을 가지고 있을 것으로 전망된다. 해리포터 시리즈의 매력에 빠져든 독자들은 해리와 친구들의 모험이 대된다.
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
    print (response)
    return response.output_parsed

# ─────────────────────────────────────────────
# 실행
# ─────────────────────────────────────────────
if __name__ == "__main__":
    summary = extract_story_structure(FULL_TEXT)
    print(summary)
