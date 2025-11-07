
FROM python:3.10
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 01d6083af2facae74b371780d996693b7d07205d
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
<<<<<<< HEAD
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
=======
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
=======
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install requirements.txt
COPY ./app /code/app
CMD ["fastapi", "run", "app/main.py", "--port", "80"]

