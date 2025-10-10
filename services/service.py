import openai
from configuration.config import OPENAI_API_KEY,MIXTRAL_API_KEY,MIXTRAL_API_URL,GEMINI_API_KEY
import requests
# from openai import OpenAI 
import google.generativeai as genai
genai.configure(api_key=GEMINI_API_KEY)

# call Openai model
def call_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

#call mixtral model
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


# Call Gemini model
def call_gemini(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")  # or "gemini-pro"
    chat = model.start_chat()
    response = chat.send_message(prompt)
    return response.text

# client = OpenAI( api_key=GEMINI_API_KEY, base_url="https://generativelanguage.googleapis.com/v1beta/openai/" ) 
# def call_gemini(prompt): 
#     response = client.chat.completions.create(
#         model="gemini-2.0-flash", 
#         messages=[ {"role": "system", "content": "You are a helpful assistant."}, 
#                   { "role": "user", "content": prompt } ] ) 
#     return response.choices[0].message 
