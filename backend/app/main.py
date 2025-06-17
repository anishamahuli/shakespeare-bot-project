from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

app = FastAPI()

# Set up CORS middleware
# This is necessary to allow frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    # allow_origins=["http://localhost:3000"],
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.get("/")
def root():
    return RedirectResponse(url="/docs")

# Load the model from Hugging Face
# model_name = "amahuli/shakespeare-llm"
tokenizer = GPT2Tokenizer.from_pretrained("amahuli/shakespeare-llm")
model = GPT2LMHeadModel.from_pretrained("amahuli/shakespeare-llm")
model.eval()
model = torch.compile(model)  # Compile the model for better performance

class Prompt(BaseModel):
    text: str

@app.post("/generate")
async def generate_text(prompt: Prompt):
    inputs = tokenizer(prompt.text, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(
        **inputs,
        max_new_tokens=50,
        use_cache=True,
        do_sample=True,
        top_k=50,
        top_p=0.95
)
    generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": generated}

