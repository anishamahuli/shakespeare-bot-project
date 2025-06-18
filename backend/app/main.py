from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

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


# app.mount("/", StaticFiles(directory=frontend_path, html=True), name="static")
frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../frontend/build"))
print("🚀 Serving frontend from:", frontend_path)
assert os.path.isdir(frontend_path), f"❌ Frontend path does not exist: {frontend_path}"

# app.mount("/static", StaticFiles(directory=frontend_path, html=True), name="static")
app.mount("/static", StaticFiles(directory=os.path.join(frontend_path, "static")), name="static")


# Catch-all for serving index.html for React SPA
@app.get("/{full_path:path}")
async def serve_react_app():
    return FileResponse(os.path.join(frontend_path, "index.html"))
