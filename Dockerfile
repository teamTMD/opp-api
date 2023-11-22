FROM python:3.11


WORKDIR /app

# Copy the requirements.txt file first to avoid rebuilding the image
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]