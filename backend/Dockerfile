### Stage 1: Build React frontend
FROM node:18 AS frontend-builder

WORKDIR /frontend

COPY frontend/ ./

RUN npm install && npm run build

### Stage 2: Backend with FastAPI + micromamba
FROM mambaorg/micromamba:1.4.2

WORKDIR /app

# Copy and create Conda env
COPY backend/environment.yml /tmp/environment.yml
RUN micromamba env create -f /tmp/environment.yml

# Activate torch-nightly for next commands
SHELL ["micromamba", "run", "-n", "torch-nightly", "/bin/bash", "-c"]

# Copy backend app
COPY backend/app ./app

# Copy built frontend from stage 1 into backend's static dir
COPY --from=frontend-builder /frontend/build ./app/static

EXPOSE 8000

CMD ["micromamba", "run", "-n", "torch-nightly", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
