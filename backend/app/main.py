from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

app = FastAPI()

@app.get("/")
def root():
    return RedirectResponse(url="/docs")


# Load your model from Hugging Face
# model_name = "amahuli/shakespeare-llm"
tokenizer = GPT2Tokenizer.from_pretrained("amahuli/shakespeare-llm")
model = GPT2LMHeadModel.from_pretrained("amahuli/shakespeare-llm")
model.eval()

class Prompt(BaseModel):
    text: str

@app.post("/generate")
def generate_text(prompt: Prompt):
    inputs = tokenizer(prompt.text, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=100)
    generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": generated}
