# Bank System Dockerization

This repository contains a Dockerized application for a simple banking system API using FastAPI.

## Table of Contents

- [Source Code](#source-code)
- [Dockerfile](#dockerfile)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Building the Docker Image](#building-the-docker-image)
  - [Running the Docker Container](#running-the-docker-container)
- [Usage](#usage)
  - [Accessing the API](#accessing-the-api)
- [Dependencies](#dependencies)
- [Ouput](#output)

## Source Code

The source code (`main.py`) includes a basic FastAPI application that provides an API endpoint to fetch account details.

## Dockerfile

The Dockerfile builds a container for the FastAPI application, exposing port 8000.

```dockerfile
FROM python:3.12-slim
RUN useradd -m nonrootuser 
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN chown -R nonrootuser:nonrootuser /app

RUN apt-get update && apt-get install -y \
    watch \
    htop \
    nano \
    curl \
    && rm -rf /var/lib/apt/lists/*
    
USER nonrootuser
EXPOSE 8000

# Run uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Getting Started

Follow these instructions to build and run the Docker containerized application.

### Prerequisites

Ensure you have Docker installed on your local machine. You can install Docker from [here](https://docs.docker.com/get-docker/).

### Building the Docker Image

1. Clone the repository:

   ```bash
   git clone https://github.com/Pranjeban/Bank-System-Dockerization.git
   cd bank_system_dockerization
   ```

2. Build the Docker image:

   ```bash
   docker build -t bank_system_image .
   ```

### Running the Docker Container

Run the Docker container:

```bash
docker run -itd --name bank_system_container -p 8000:8000 bank_system_image
```

The application will be accessible at `http://localhost:8000`.

## Usage

### Accessing the API

- **Root Endpoint:**

  ```http
  GET /
  ```

  Response:
  ```json
  {"message": "Welcome to the Bank System API"}
  ```

- **Account Endpoint:**

  ```http
  GET /accounts/{account_id}
  ```

  Replace `{account_id}` with a valid integer account ID to fetch account details.

## Dependencies

- Python 3.10 or higher
- FastAPI
- Uvicorn

## Install dependencies from requirements.txt:

```bash
pip install -r requirements.txt
```

## Ouput

# Fetching Data From Database
![Alt-text](./output_images/Screenshot%20from%202024-07-09%2021-24-27.png)

# Inserting Data To the Database 
![Alt-text](./output_images/Screenshot%20from%202024-07-09%2021-25-02.png)