import openai
from configuration.config import OPENAI_API_KEY,MIXTRAL_API_KEY,MIXTRAL_API_URL,GEMINI_API_KEY
import requests
from openai import OpenAI 

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



client = OpenAI( api_key=GEMINI_API_KEY, base_url="https://generativelanguage.googleapis.com/v1beta/openai/" ) 
def call_gemini(prompt): 
    response = client.chat.completions.create(
        model="gemini-2.0-flash", 
        messages=[ {"role": "system", "content": "You are a helpful assistant."}, 
                  { "role": "user", "content": prompt } ] ) 
    return response.choices[0].message 
