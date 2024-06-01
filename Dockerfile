FROM python:3.11.9-slim

# Set the working directory
ENV PYTHONUNBUFFERED=1

ARG DEBIAN_FRONTEND=noninteractive

# Install Firefox binary
#RUN apt-get update && \
#    apt-get install -y build-essential libffi-dev libssl-dev python3-dev && \
#    apt-get install -y firefox-esr --no-install-recommends && \
#    rm -rf /var/lib/apt/lists/* && \
#    apt-get install -yq tzdata && \
#    ln -fs /usr/share/zoneinfo/Asia/Ho_Chi_Minh /etc/localtime && \
#    dpkg-reconfigure -f noninteractive tzdata

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
RUN robot -d results test_case/login_tests;


#run python main.py

CMD ["python", "main.py"]
