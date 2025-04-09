import openai
from configuration.config import OPENAI_API_KEY,MIXTRAL_API_KEY,MIXTRAL_API_URL
import requests

def call_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def call_mixtral(prompt):
    headers = {
        "Authorization": f"Bearer {MIXTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mixtral-8x7b",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(MIXTRAL_API_URL, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"].strip()