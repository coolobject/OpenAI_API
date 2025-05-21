from openai import OpenAI
#-----------------
# set OPENAI_API_KEY 
#-----------------
from dotenv import load_dotenv
import os

load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

model_s="gpt-4.1-nano-2025-04-14"
model_m = "gpt-4.1"
#-----------------

client = OpenAI()

response = client.responses.create(
    model=model_m,
    tools=[{"type": "web_search_preview"}],
    input="What was the weather like in Seoul today? (using under 20 words)"
)

print(response.output_text)