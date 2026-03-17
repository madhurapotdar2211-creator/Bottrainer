import os
import json

import ollama
from dotenv import load_dotenv
print("dotenv working")
load_dotenv()

def load_prompt(text):
    with open("prompts/intent_prompt.txt", "r") as file:
        template = file.read()
    return template.replace("{input}", text)



def get_llm_response(text):

    with open("prompts/intent_prompt.txt") as f:
        prompt = f.read()

    prompt = prompt.replace("{input}", text)

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]

    try:
        return json.loads(content)
    except:
        return {
            "intent": "unknown",
            "confidence": 0.0,
            "entities": {}
        }