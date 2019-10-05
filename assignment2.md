## Assignment 2
![Assignment 2](https://i.imgur.com/yUh5NT4.png)

```
# install ubuntu 14.04
docker container run -it --name ubuntu ubuntu:14.04 "/bin/bash"

# install centos 7
docker container run -it --name centos centos:7 "/bin/bash"
```
But as soon as I exit the container, the container stops running. Running `docker container ls -a` shows `Exited (0) seconds ago` status.

