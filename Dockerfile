FROM python:3.10
#EXPOSE 5000
WORKDIR /
COPY ./requirements.txt
RUN  pip install --no-cache-dir --upgrade -r /requirements.txt
COPY ./app
CMD ["fastapi", "run", "app/main.py", "--port", "80"]
