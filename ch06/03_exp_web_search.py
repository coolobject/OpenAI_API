from openai import OpenAI
#-----------------
# set OPENAI_API_KEY 
#-----------------
from dotenv import load_dotenv
import os

load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

MODEL_4o ="gpt-4.o"
MODEL_4_1 = "gpt-4.1"
MODEL_SEARCH = "gpt-4o-search-preview"
#-----------------

client = OpenAI()

response = client.responses.create(
    model=MODEL_4_1,
    tools=[{"type": "web_search_preview"}],
    input="오늘은 2025년 6월 5일인데요, 종로구 날씨를 알려주세요."
)

print(response.output_text)