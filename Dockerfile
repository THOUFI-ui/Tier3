FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application package
COPY app/ app/

# Copy config and entrypoint
COPY config.py .
COPY wsgi.py .

EXPOSE 5000

CMD ["python", "wsgi.py"]
