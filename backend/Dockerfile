FROM mambaorg/micromamba:1.4.2

WORKDIR /app

COPY environment.yml /tmp/environment.yml

# Create the environment using micromamba
RUN micromamba env create -f /tmp/environment.yml

# Activate the environment in future commands
SHELL ["micromamba", "run", "-n", "torch-nightly", "/bin/bash", "-c"]

# Copy app code
COPY app ./app

EXPOSE 8000

# Start the FastAPI app
CMD ["micromamba", "run", "-n", "torch-nightly", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
