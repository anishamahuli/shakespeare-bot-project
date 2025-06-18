FROM mambaorg/micromamba:1.4.2

# Set working directory
WORKDIR /app

# Copy environment file and create conda environment
COPY backend/environment.yml /tmp/environment.yml
RUN micromamba env create -f /tmp/environment.yml

# Activate environment for all subsequent commands
SHELL ["micromamba", "run", "-n", "torch-nightly", "/bin/bash", "-c"]

# Copy backend code
COPY backend/app ./app

# Copy built frontend static files (make sure you ran `npm run build` before building this image)
COPY frontend/build ./frontend/build

# Expose FastAPI port
EXPOSE 8000

# Run uvicorn to serve your FastAPI app
CMD ["micromamba", "run", "-n", "torch-nightly", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
