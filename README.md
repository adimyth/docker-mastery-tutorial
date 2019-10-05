# Docker
Docker is a platform to develop, deploy and run applications with containers.

## Images vs Containers
* Image is the binaries, libraries & source code that make up an application
* A container is a running instance of an image that runs as a process
* You can have many containers running of the same image
* Image registry is for container images what GitHub is for source code. Default is Docker Hub

## What happens in "`docker container run`"
1. Looks for the image locally in image cache
2. If it couldn't find the image, then it looks in remote repository (Docker Hub)
3. Download the latest version of the image
4. Creates a new container based on that image & prepares to start
5. Gives the container a virtual IP on a private network inside docker engine
6. Starts container by using the **"CMD"** in Dockerfile

## Containers?
* Containers are runtime instances of images - what the image becomes in memory when executed
* They are not Virtual Machines
* They are simply processes running on the host OS. You can view the containers running as processes in the host operating system using `ps aux | grep container_name`
* They can be manipulated like any other process

## Process Monitoring
* `docker container top` - lists all the process inside a container
* `docker container inspect` - details of one container config. Provides metadata
* `docker container stats` - performance stats of all containers

## Getting a shell inside a container
`docker container run` always starts a new container as a process. `docker container start` allows us to start an existing stopped container. 

```bash
docker container run -it "bash"
```
* i - interactive
* t - tty

Here, we get an interactive shell inside the container. `run -it` starts a new container interactively. `bash` here is the command that gets run when the container starts. 

```bash
docker container exec -it "bash"
```
* i - interactive
* t -tty

Again, we get an interactive shell inside an existing container. `exec -it` does not start a new container & runs additional command in existing container. 

## Docker Networks
* Each connector get connected to a private virtual network "Bridge" by default
* All containers on a virtual network with each other without exposing the port 
* `docker container run -p` exposes the port on local host to the container
* `docker container port` - gives the list of ports open on the container
* Skip virtual networks and use host `(--net=host)`
* On your localhost you cannot listen on one port for multiple containers i.e. you cannot use `docker container run -p` option for running multiple containers using the same port

```
docker network ls
```
* Bridge - Default virtual network where containers get attached
* Host - Skips virtual network & the container attaches itself directly to the host network
* Null - Is not connected to any network

```
docker network inspect bridge
```
By default the `Subnet` for docker containers is `172.17.0.0` & `Gateway: 172.17.0.1`. Also, we can see the containers attached to this virtual network under the `"Containers"` section.

```
docker network create my_app_net
```
Creates a new virtual network `my_app_net` with the default driver `bridge`. 

```
docker container run -d --name new_nginx --network my_app_net nginx
```
Creates a new nginx container & attaches itself to the `my_app_net` network. Can by verified by running `docker network inspect my_app_net`

```
docker network connect my_app_net webhost 
```
Just like changing networks in real world, we can change the virtual networks for the containers too.

### Docker DNS
Containers on a network can talk to each other easily. Multiple containers on a single private virtual network can't rely on static IP addresses to communicate with each other, as they are very dynamic. Creating `n` different containers on the same virtual network assigns each container different IP address every time they are created in different order.

**Docker uses container names as the equivalent of host names for containers talking to each other**

Example -

```
# creating first container on a new virtual network
docker container run --name nginx_one -d --network my_app_net nginx

# creating another container on the same network
docker container run --name nginx_two -d --network my_app_net nginx

# ping one of the containers from other
docker container exec -it nginx_one ping -c 5 nginx_two
```
We can enable this on default network `bridge` using the `--link` option. Notice, that you might need to install `inetutils-ping` in the container "nginx_one".

```
docker container run -d --name elasticsearch  --network my_app_net --net-alias elasticsearch_dns elasticsearch:2
```
`--net-alias aliasname` allows you to change the DNS name from the default container name provided by `--name` option to `aliasname`. This is specially useful when there are multiple containers or multiple versions of the same application connected to a single virtual network & you wish to respond both of them incase we make a request on a particular DNS.

## Docker Images
`docker image ls` - List docker images
`docker image history` - Shows history of layers in an image

### Layers
A docker image consists of read-only layers. The **Docker storage driver** stacks and maintains the different layers. The storage driver also manages sharing of layers across images. This makes building, pulling, pushing, and copying of images fast and saves on storage. When a container is run using `docker container run`, each docker gets a writeable layer and all changes are stored in this layer. It is possible for multiple images to share the same layers.

Once the container is deleted, all the data is lost. If we wish to store the data on this writeable layer, we can mount host's filesystem directly into the container. When building a container from an image, we get one intermediate layer for every instruction. These intermediate layers allow for faster builds, smaller image sizes and easy rollbacks.

When we build an image using Dockerfile, it is built in top-down fashion. Order of the commands matter.

```
docker build -t [tag] Dockerfile
```
Builds a container from a docker file

```
docker build tag [source_tag] [target_tag]
```
Creates a duplicate of an existing container with tag changed from `source_tag` to `previous_tag`

## Container lifetime
* Containers are usually immutable(unchanging) and ephemeral(short life cycles)
* Design Goal - Disposable containers that can be recreated using the image.
* Immutable Infrastructure - We do not change things once they are running & if the container needs to be upgraded, then we re-deploy the containers
* Separation of concerns
* Containers by default are persistent i.e any changes made in the container are persistent across reboots or host restart unless we remove the container. Just because we restart the container, doesn't means that it's data will go away. Only when we remove the container, it's UFS layer goes away. 
	* Data Volumes - We provide a special location outside the container to UFS to store unique data, which is preserved across container removals & can be attached to any other container that we wish to.
	* Bind Mounts - Here, we mount a host directory into a container. The container treats it just like a local filesystem. 

### Volumes
Volumes are actual mounts on the host system. They need manual cleanup, they cannot be removed just by removing the container.

> VOLUME command in Dockerfile

> docker container run **-v mysql-db:/var/lib/mysql** -d mysql

```
docker container inspect mysql_container
```
Notice the `Source` & `Destination` options in the `Mount` section. The `Destination` is where the container thinks is writing the data. It is the same as `VOLUME` provided in Dockerfile. However, the data is actually stored at `Source`.

```
docker volume ls
docker volume inspect volume_id
```
Docker volume listing doesn't provide any information about the container with which that volume is linked. Hence, we use **named volumes**

```
docker container run -v mysql-db:/var/lib/mysql -d -e MYSQL_ALLOW_EMPTY_PASSWORD=True mysql
```
This creates a new entry in volume listing with name `mysql-db`. 

### Bind Mounts
* Maps a file or directory in host to a file or directory inside a container.
* Basically, it's two locations pointing to the same file.
* If we make a change to the file or the directory at the bind mount using either the container or the host, the change is reflected on the other side.
* Data is persistent to removal & destroyal of containers. 
* Can't be specified in Dockerfile, but use `-v` option while running the `docker container run`
* However, it doesn't get reflected in `docker volume ls`. But we can get that info using `volume inspect` command.  Example - navigate to `dockerfile-sample-2`

```
docker container run -d --name nginx_mount -p 8080:80 -v $(pwd):/usr/share/nginx/html nginx

# see the updated index.html
curl localhost:8080
```

## Docker Compose
In real world situations, we are rarely gonna use single container solutions. We usually require multiple application containers running simultaneously & communicating with each other. For example, sql container, proxy, etc. Docker Compose synchronises the communication/relationship between containers.

