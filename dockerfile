# Use an official Python runtime as the base image
FROM python:3.9-slim

# Install required packages for Selenium, Chrome, and ChromeDriver
RUN apt-get update && \
    apt-get install -y curl gnupg unzip libnss3 libgconf-2-4 && \
    rm -rf /var/lib/apt/lists/*

# Add the Google Chrome APT repository and install Chrome
RUN curl -fsSL https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-linux-keyring.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-linux-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*


# Download the specific ChromeDriver version
RUN wget https://chromedriver.storage.googleapis.com/131.0.6778.69/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver && \
    rm chromedriver_linux64.zip
# Set environment variables for Chrome and ChromeDriver
ENV CHROME_BIN=/usr/bin/google-chrome \
    CHROME_DRIVER=/usr/local/bin/chromedriver

# Set working directory
WORKDIR /app


# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the app
COPY . /app
WORKDIR /app

# Default command
CMD ["python", "-m", "unittest", "discover", "-s", "."]
