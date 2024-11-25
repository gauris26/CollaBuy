import os
from dotenv import load_dotenv
from openai import OpenAI
from utils.constants import SYSTEM_PROMPT

def generate_json(prompt: str) -> str:
    load_dotenv()
    AI_ML_API_KEY = os.getenv('AI_ML_API_KEY')
    client = OpenAI(
      api_key = AI_ML_API_KEY,
      base_url = "https://api.aimlapi.com",
    )

    response = client.chat.completions.create(
        model="meta-llama/Llama-3.2-3B-Instruct-Turbo",
        max_tokens=5000,
        temperature=0.1,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            },
        ],
    )

    return  response.choices[0].message.content.strip()