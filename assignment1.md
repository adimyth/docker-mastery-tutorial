## Assignment 1 

![Assignment 1](https://i.imgur.com/wnFzHIk.png)
#### Running nginx container
```bash
# pulls nginx image from docker hub & port forwards request on port 80 at local host to container
docker container run -p 80:80 -d --name nginx_container nginx

# validating
docker container ls -a

# hit localhost:80 several times & check logs
docker container logs nginx_container

# stopping the container
docker container stop nginx_container

# remove the container
docker container rm nginx_container
```
#### Running mysql container
```bash
# pulls mysql image from docker hub & port forwards request on port 3306 on localhost to 3306 port on the container
docker container run -p 3306:3306 -d --name mysql_container -e MYSQL_RANDOM_ROOT_PASSWORD=yes

# check logs for password (gaepeeXaisoosh1ziel7yie7Eivei8ha)
docker container logs mysql_container 

# stop the container
docker container stop mysql_container

# remove the container
docker container rm mysql_container
```
