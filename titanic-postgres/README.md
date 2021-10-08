# Repo for creating Titanic Postgres DB
        .
    ├── Dockerfile
    ├── README.md
    ├── init-user-db.sh
    └── titanic.csv

    Dockerfile uses postgresql:11.5.0 from bitnami
    init-user-db.sh is a shell script which is copied to /docker-entrypoint-initdb.d/ inside postgres image which is picked up when container starts and db is initilaized with this data (titanic.csv).

# Steps to build and the repo to push the image
    `docker build . -t <YOUR_DOCKER_REPO>`
    `docker push `<YOUR_DOCKER_REPO>`
# To run the postgres container

    It requires postgres 11.5.0 . Also the following environment variables are required for the postgres to start.You may also need to specify any additional variables or arguments if required

    | Environment Variables  | Description                                             |
    | -----------------------| ------------------------------------------------------- |
    | POSTGRES_USER          | Username required to connect to postgres database       |
    | POSTGRES_PASSWORD      | Password required to connect to postgres database       |
    | POSTGRES_DB            | Database name required to connect to postgres database  |