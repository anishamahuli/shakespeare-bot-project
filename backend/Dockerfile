FROM conda/miniconda3

# Set working directory
WORKDIR /app

# Copy env and install
COPY environment.yml .
RUN conda env create -f environment.yml

# Activate env by default
SHELL ["conda", "run", "-n", "torch-nightly", "/bin/bash", "-c"]

# Install FastAPI app dependencies
COPY app ./app

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI using uvicorn in the conda env
CMD ["conda", "run", "--no-capture-output", "-n", "torch-nightly", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
