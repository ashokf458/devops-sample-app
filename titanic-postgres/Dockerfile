FROM postgres:12.0

COPY ./init-user-db.sh /docker-entrypoint-initdb.d
COPY ./titanic.csv /docker-entrypoint-initdb.d
