# Use the latest Ubuntu image as the base image
FROM ubuntu:latest

# Set environment variables to avoid interactive prompts during package installations
ENV DEBIAN_FRONTEND=noninteractive

# Install required dependencies (including Python, Chrome, and necessary libraries)
RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    wget \
    curl \
    gnupg \
    ca-certificates \
    unzip \
    libx11-dev \
    libxkbcommon-dev \
    libgdk-pixbuf2.0-dev \
    libnss3 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libgdk-pixbuf2.0-0 \
    libxss1 \
    libasound2 \
    fonts-liberation \
    libappindicator3-1 \
    libnspr4 \
    libxcomposite1 \
    libxrandr2 \
    xdg-utils \
    && apt-get clean

# Install Google Chrome (latest stable version)
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o google-chrome-stable.deb && \
    dpkg -i google-chrome-stable.deb && \
    apt-get install -f -y && \
    rm google-chrome-stable.deb

# Install ChromeDriver (latest version)
RUN LATEST=$(curl -sSL https://chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget https://chromedriver.storage.googleapis.com/$LATEST/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin/ && \
    rm chromedriver_linux64.zip

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any Python dependencies from requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Define the command to run your app
CMD ["python3", "main.py"]  # Change main.py to your entry point
