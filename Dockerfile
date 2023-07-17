FROM python:3.11-slim-bullseye

RUN apt-get update && \
		apt-get install -y --no-install-recommends \
		curl \
		build-essential

# Install Rust and Rye
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

WORKDIR /my-python-samples

COPY requirements.txt /
RUN pip install -r /requirements.txt && \
		virtualenv .venv

COPY . .
