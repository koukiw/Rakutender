# ビルド用コンテナ
FROM python:3.9-buster as builder

COPY ./requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# 実行用コンテナ
FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y \
  vim wget build-essential gcc zlib1g-dev

COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/uvicorn

ENV TZ Asia/Tokyo

COPY ./api/ /api


