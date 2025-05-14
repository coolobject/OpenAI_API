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
    model=model_s,
    input=[
        {"role": "user", "content": "what's this character's name in this image?"},
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