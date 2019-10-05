## Assignment 3
```
# create a new network
docker create network my_new_network --driver bridge

# run the first elasticsearch container
docker container run -d--name elastic_search_first --network my_new_network --net-alias elastic_search elasticsearch:2

# run the second elasticsearch container
docker container run -d --name elastic_search_second --network my_new_network --net-alias elastic_search elasticsearch:2

# check if they are running
docker container ls

# create & run alpine container
docker container run -it --name alpine --network my_new_network alpine "sh"

# get an interactive shell in the container
docker container exec -it alpine "sh"

# nslookup for the given DNS alias name
nslookup elastic_search

# run centos docker
docker container run -it --name centos --network my_new_network centos:7

# inside centos
curl -s elastic_search:9200
```

