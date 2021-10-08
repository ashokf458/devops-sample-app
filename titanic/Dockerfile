FROM python:3.7

ENV POSTGRES_USER='pg_user'
ENV POSTGRES_PASSWORD='pg_pass'
ENV POSTGRES_HOST='pg_host'
ENV POSTGRES_PORT='5432'
ENV POSTGRES_DB='pg_db'

COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY ./ /opt/titanic

WORKDIR /opt/titanic

CMD ["server.py"]
ENTRYPOINT ["python"]
