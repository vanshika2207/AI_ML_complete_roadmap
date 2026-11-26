FROM python:3.12

WORKDIR /app

RUN pip install flask debugpy

COPY . .

EXPOSE 5000
EXPOSE 5070

CMD ["flask", "run", "--host=0.0.0.0"]