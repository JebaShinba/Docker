# Use an official Python runtime as the base image
FROM python:3.9-slim

# Install required packages for Selenium and Chrome
RUN apt-get update && \
    apt-get install -y unzip curl && \
    apt-get install -y libnss3 libgconf-2-4 && \
    rm -rf /var/lib/apt/lists/*

# Install Chrome browser
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb && \
    apt-get install -y ./chrome.deb && \
    rm chrome.deb

# Install ChromeDriver
RUN CHROME_DRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    curl -sSL "https://chromedriver.storage.googleapis.com/${CHROME_DRIVER_VERSION}/chromedriver_linux64.zip" -o chromedriver.zip && \
    unzip chromedriver.zip -d /usr/local/bin/ && \
    rm chromedriver.zip

# Set environment variables for Chrome and ChromeDriver
ENV CHROME_BIN=/usr/bin/google-chrome \
    CHROME_DRIVER=/usr/local/bin/chromedriver

# Set working directory
WORKDIR /app

# Copy Python dependencies and install them
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy the test code
COPY . /app

# Run the test suite using unittest when the container starts
CMD ["python", "-m", "unittest", "discover", "-s", "."]
