#!/bin/bash
set -e
ls -ltrh /docker-entrypoint-initdb.d/
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    create type sex_t as enum('male', 'female', 'other');
    CREATE TABLE passengers (  
    id SERIAL NOT NULL PRIMARY KEY, 
    survived BOOLEAN,
    passengerclass INT,
    name VARCHAR(255),
    sex sex_t,
    age FLOAT8,
    siblingsorspousesaboard INT,
    parentsorchildrenaboard INT,
    fare FLOAT8
    );
    \copy passengers (survived, passengerClass, name, sex, age, siblingsorspousesaboard, parentsorchildrenaboard, fare) from '/docker-entrypoint-initdb.d/titanic.csv' CSV HEADER;
EOSQL