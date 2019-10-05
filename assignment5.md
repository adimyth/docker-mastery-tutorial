## Assignment 5: Named Volumes
Very important & interesting exercise, as it shows that even updating a container allows us to persist with data
![Assignment 5](https://i.imgur.com/8mXrswl.png)

```
# create a container using postgres-9.6.1 & named volumes
docker container run -d --name postgres -v psql-data:/var/lib/postgresql/data postgres:9.6.1

# check logs => there's many stuffs here
docker container logs postgres

# stop the running container
docker container stop postgres

# create an updated version of container using Postgres-9.6.2 using the same volume mount
docker container run -d --name postgres_new -v psql-data:/var/lib/postgresql/data postgres:9.6.2

# check the logs => many of the stuff has already happened, so here's barely anything
docker container logs postgres_new
```

