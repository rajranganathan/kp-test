FROM python:3.7-slim
RUN pip install flask
WORKDIR /app
COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt
RUN ls /app/app.py
RUN pip install -r /app/requirements.txt
ENTRYPOINT ["python"]
CMD ["/app/app.py"]
