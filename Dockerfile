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