FROM python:3.11.9-slim

# Set the working directory
ENV PYTHONUNBUFFERED=1

ARG DEBIAN_FRONTEND=noninteractive

# Install Firefox and Geckodriver
RUN apt-get update && apt-get install -y \
    wget \
    firefox-esr --no-install-recommends \
    && wget https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz \
    && tar -xzf geckodriver-v0.33.0-linux64.tar.gz -C /usr/local/bin \
    && rm geckodriver-v0.33.0-linux64.tar.gz

# Set display environment (for headless execution)
ENV DISPLAY=:99

# Install Xvfb for virtual display
RUN apt-get install -y xvfb

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Install pip requirements
WORKDIR /app

COPY requirements.txt  ./
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt


COPY . ./


# run robot tests_cases
RUN robot -d results test_case/login_tests; exit 0;


#run python main.py

CMD ["python", "main.py"]
