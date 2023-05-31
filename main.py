import openai
from dotenv import load_dotenv
import os
from langchain.llms import OpenAI
from langchain import LLMChain
from langchain.prompts import PromptTemplate
from prompt import validator_prompt_template

from fastapi import FastAPI

app = FastAPI()

load_dotenv()

# Access the environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0,model_name='gpt-3.5-turbo',max_tokens=1000)
chain_valid = LLMChain(prompt=validator_prompt_template,llm=llm)

@app.get('/')
def home():
    return {"Validator":"App"}

@app.post("/validate")
def validate_responses(sentence1: str, sentence2: str):
    result = chain_valid.run({'sentence1': sentence1, 'sentence2': sentence2})
    return result




