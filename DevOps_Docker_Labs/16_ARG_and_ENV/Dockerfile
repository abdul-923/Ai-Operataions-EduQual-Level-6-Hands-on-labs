
FROM python:3.9-slim

ARG APP_VERSION=1.0.0

ENV APP_ENV=production

RUN echo "Building versiob $APP_VERSION"

WORKDIR /app

COPY . /app

CMD ["python" , "app.py"]


