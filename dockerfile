FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5001 


CMD ["python", "app.py"]
