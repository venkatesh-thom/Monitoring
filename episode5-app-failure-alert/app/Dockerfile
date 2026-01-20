FROM python:3.11-slim

RUN useradd -m appuser

WORKDIR /app

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY app.py .

USER appuser
EXPOSE 5000
CMD ["python", "app.py"]
