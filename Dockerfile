FROM python:3.11

WORKDIR "$APP_HOME"

COPY . .

RUN pip install -r ./requirements.txt

EXPOSE 8080

CMD ["python3", "app.py"]