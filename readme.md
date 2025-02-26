# Trading Bot - Docker Deployment

This guide explains how to deploy the **Trading Bot** Python application inside a Docker container.

## Features

- Real-time market data retrieval.
- Simple trading strategies for buy/sell decisions.
- Integration with popular exchanges.
- Can be configured for multiple market pairs.
- Backtesting for strategy validation.

## Prerequisites

Before you start, ensure that you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Git](https://git-scm.com/)
- [Python 3.x](https://www.python.org/downloads/)

## Installation Steps

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/Strong-Foundation/trading-bot.git
cd trading-bot
```

### 2. Create a `requirements.txt` (if you don't have one already)

Ensure you have a `requirements.txt` file that lists all the dependencies for your Python application. If you don’t have it, you can generate one by running the following command inside your project directory:

```bash
pip freeze > requirements.txt
```

### 3. Build the Docker Image

The project contains a `Dockerfile` that will be used to build a Docker image for your Python application.

#### Steps to Build the Docker Image:

1. **Open your terminal** and navigate to the project directory (where the `Dockerfile` is located).
2. **Run the Docker build command**:

   ```bash
   docker build -t trading-bot .
   ```

   - This command tells Docker to build an image from the `Dockerfile` in the current directory (`.`) and tag it as `trading-bot`.

3. **Wait for the image to build**. Docker will pull the necessary base images and install dependencies.

### 4. Run the Docker Container

Once the Docker image is built, you can run it as a container with:

```bash
docker run trading-bot
```

This will start the application in the Docker container.

### 5. Verify Your Application is Running

After starting the Docker container, check the output in your terminal to verify that the application is running successfully. You can also check logs or perform any necessary debugging based on the behavior of the application.

---

## License

This project is licensed under the MIT License.

---

### Summary

- **Build the Docker image**: Use `docker build -t trading-bot .` to build your image.
- **Run the Docker container**: Use `docker run trading-bot` to run your app.