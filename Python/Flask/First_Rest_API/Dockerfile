FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
EXPOSE 5070

CMD ["flask", "run", "--host=0.0.0.0"]