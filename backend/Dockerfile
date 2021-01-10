FROM python:3
ENV PYTHONUNBUFFERED 1

WORKDIR /opt/backend

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY backend .

EXPOSE 8000