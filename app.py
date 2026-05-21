from fastapi import FastAPI
from transformers import pipeline 


app=FastAPI()

pipe=pipeline("text-generation",model="gpt2") # you can change the model to any other text generation model available in Hugging Face

@app.get('/')
def home():
    return {"message": "Hello LLM"}

@app.get("/generate")
def generate(text:str):
    '''use the pipeline to generate text'''
    output = pipe(text)
    return {"output":output[0]['generated_text']}

