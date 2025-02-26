# Use the latest Ubuntu image as the base image
FROM ubuntu:latest

# Set environment variables to avoid interactive prompts during package installations
ENV DEBIAN_FRONTEND=noninteractive

# Install Python and dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    apt-get clean

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose the port your app will run on (change if needed)
EXPOSE 5000

# Define the command to run your app
CMD ["python3", "main.py"]  # Change main.py to your entry point
