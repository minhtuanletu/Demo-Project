Note scripts:

* Run docker image: postgres database
```
docker run -e POSTGRES_PASSWORD=123456 -e POSTGRES_USER=minhtuan -e POSTGRES_DB=demo -d -p 8989:5432 postgres
```

* Create database in postgres
```
$ psql -U minhtuan -d demo
$ create table result(
    id SERIAL PRIMARY KEY,
    label_image VARCHAR(50),
    conf decimal,
    status VARCHAR(50)
);
```