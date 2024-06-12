FROM python:3.11.4

ENV PYTHONUNBUFFERED=1

WORKDIR /code

# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy the entire project into the working directory
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
