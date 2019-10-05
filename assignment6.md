## Assignment 6: Bind Mounts
![Assignment 6](https://i.imgur.com/NMxwJK1.png)

```
cd bindmount-sample-1

# run the Jekyll-serve container 
docker container run -d --name bindmount_example -p 80:4000 -v $(pwd):/site bretfisher/jekyll-serve

# check on localhost
curl localhost:80

# check the running Jekyll server inside container
docker container exec -it bindmount_example "/bin/sh"
wget localhost:80
# check the local file contents
vi index.html
```
