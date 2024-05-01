FROM python:latest

# pythonライブラリのインストール
RUN apt-get update
RUN pip install --upgrade pip
RUN pip install psycopg2

# プロジェクト追加
ADD main.py .
ADD janken.py .
