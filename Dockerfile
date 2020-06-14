FROM python:3

WORKDIR /code

COPY requirements.txt ./
run pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "testcgi.py"]

