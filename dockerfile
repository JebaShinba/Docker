FROM python:3.9-slim

# Install Chrome and dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    chromium \
    chromium-driver

# Download the specific ChromeDriver version
RUN wget https://chromedriver.storage.googleapis.com/131.0.6778.69/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver && \
    rm chromedriver_linux64.zip

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the app
COPY . /app
WORKDIR /app

# Default command
CMD ["python", "-m", "unittest", "discover", "-s", "tests"]
