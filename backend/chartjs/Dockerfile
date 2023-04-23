FROM python:3.10-slim-buster
ENV PYTHONUNBUFFERED 1

RUN mkdir /backend
COPY . /backend/
WORKDIR /backend
EXPOSE 8000
RUN pip install -r requirements.txt
CMD python manage.py collectstatic
# ENTRYPOINT 