FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir pylint

CMD ["python", "test_calc.py"]
