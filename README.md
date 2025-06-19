# Shakespeare Bot #

A full-stack web application that generates Shakespearean-style text using a custom fine-tuned GPT-2 model. The project includes a FastAPI backend that serves the model (hosted on Hugging Face), a React frontend for users to interact with the bot, and Docker-based deployment for production readiness. 


## About the model ##
This project uses a custom fine-tuned GPT-2 model to generate text in the style of William Shakespeare. The model is hosted on Hugging Face Hub and is served via a FastAPI backend.
The base model is `GPT2LMHeadModel` from [Huggingface transformers](https://huggingface.co/docs/transformers/en/index).
The model is trained on the works of Shakespeare, including plays, sonnets, and poems. 

My model is hosted publicaly and can be accessed on [Huggingface Hub](https://huggingface.co/amahuli/shakespeare-llm). For more information about this custom model, see its [documentation](https://github.com/anishamahuli/shakespeare-llm).
During inference, the input prompt (from the user) is tokenized using the GPT-2 tokenizer. The tokenized input is passed to the model's `generate()` method with parameters for creative sampling. The output tokens are decoded back to natural language.


### Features ###
- Text generation using `GPT2LMHeadModel`, a GPT-2 model from Huggingface
- Outputs mimic Shakespearean language
- React-based UI with loading states
- FastAPI backend with async inference route
- Fully containerized with Docker

### Tools Used ###
- Transformers (by Hugging Face): for model architecture, tokenizer, and generation logic.
- PyTorch: for underlying tensor computation.
- FastAPI: for serving the model via a REST API.
- Docker: for packaging the entire backend/frontend stack.
- React: for the frontend UI where users input prompts.

### Limitations ###
- Text Quality: While stylistically Shakespearean, generated text may sometimes lack logical coherence or proper grammatical flow.
- Bias & Noise: May occasionally produce modern idioms or awkward phrasing due to the base GPT-2's pretraining on non-Shakespearean text.
- No Memory or Context: Each generation is independent—there is no persistent memory or dialogue tracking.
- Token Limit: Limited to GPT-2’s max token window (typically 1024 tokens).
- Latency: Inference time can range from 5–30 seconds depending on prompt length and generation settings, especially on CPUs.

### Inference Settings ###
These are the key generation parameters used in `main.py`:
```
outputs = model.generate(
        **inputs,
        max_new_tokens=50,
        use_cache=True,
        do_sample=True,
        top_k=50,
        top_p=0.95
)
```
- `do_sample=True`: enables sampling instead of greedy decoding.
- `top_k=50`: limits next-token selection to the top 50 highest-probability tokens.
- `top_p=0.95`: uses nucleus sampling to pick from the smallest set of tokens whose cumulative probability is ≥ 95%.
- `max_new_tokens=50`: limits the length of generated output.
- 


## Local Development ##
1. Clone the repo with `git clone https://github.com/anishamahuli/shakespeare-bot-project`
2. Build the container using `docker build -t shakespeare-api -f backend/Dockerfile .`
3. Run the container using `docker run --name shakespeare -p 8000:8000 shakespeare-api`. This may take a couple minutes.
4. Once the container is running, visit http://localhost:8000

It should look something like this
<p align="center">
<img width="551" alt="Screenshot 2025-06-19 at 12 27 41 PM" src="https://github.com/user-attachments/assets/d1053e1b-a6a5-46cb-adc6-3731ec0325ed" />
</p>


