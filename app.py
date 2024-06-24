from fastapi import FastAPI
from transformers import pipeline 


app=FastAPI()

pipe=pipeline("text2text-generation",model="google/flan-t5-small")

@app.get('/')
def home():
    return {"message": "Hello LLM"}

@app.get("/generate")
def generate(text:str):
    '''use the pipeline to generate text'''
    output = pipe(text)
    return {"output":output[0]['generated_text']}

