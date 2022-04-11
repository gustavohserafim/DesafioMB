FROM python:3.10

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt update
RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install -r ./requirements.txt --no-cache-dir
ADD . /app
RUN chmod +x sources/entry-point.sh
EXPOSE 5000
ENTRYPOINT ["/sources/entry-point.sh"]