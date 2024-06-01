FROM python:3.11.9-slim

# Set the working directory
ENV PYTHONUNBUFFERED=1

ARG DEBIAN_FRONTEND=noninteractive

# Install Firefox binary
RUN apt-get update && \
    apt-get install -y build-essential libffi-dev libssl-dev python3-dev && \
    apt-get install -y firefox-esr --no-install-recommends && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get install -yq tzdata && \
    ln -fs /usr/share/zoneinfo/Asia/Ho_Chi_Minh /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# Install pip requirements
WORKDIR /app

COPY requirements.txt  ./
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt


COPY . ./


# run robot tests_cases
RUN robot --headless test_case/login_tests; exit 0


#run python main.py

CMD ["python", "main.py"]
