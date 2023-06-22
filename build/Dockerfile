FROM python:3.11.4-alpine3.17

WORKDIR /app
ADD src /app/src
RUN pip install --upgrade pip
RUN pip install -r src/requirements.txt
CMD ["python3", "src/main.py"]

