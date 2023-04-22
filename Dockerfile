FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000 

CMD ["flask", "--app", "src/rock_paper_scissors/app", "run", "-h", "0.0.0.0", "port=3000"]


