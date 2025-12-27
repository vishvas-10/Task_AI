import os
from openai import OpenAI

def get_llm_client()->OpenAI:
    '''returns a openai compatible client'''
    return OpenAI(
        api_key=os.environ['OPEN_AI_API'],
        base_url="https://api.groq.com/openai/v1"
    )