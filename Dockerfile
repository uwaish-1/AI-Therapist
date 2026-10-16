# Use Python 3.13
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libportaudio2 \
    portaudio19-dev \
    gcc \
    g++ \
    libc-dev \
    make \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install --no-cache-dir uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies using the locked versions
RUN uv sync --frozen --no-dev --no-install-project

# Copy application code
COPY . .

# Streamlit port
EXPOSE 8501

# Start Streamlit
CMD ["uv", "run", "--no-sync", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
