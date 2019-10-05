## Assignment 4
![Assignment 4](https://i.imgur.com/xtJXnDW.png)
Dockerfile

```
# - you should use the 'node' official image, with the alpine 6.x branch
FROM node:6-alpine

# - this app listens on port 3000, but the container should launch on port 80
#  so it will respond to http://localhost:80 on your computer
EXPOSE 3000

# - then it should use alpine package manager to install tini: 'apk add --update tini'
RUN apk add --update tini

# - then it should create directory /usr/src/app for app files with 'mkdir -p /usr/src/app'
WORKDIR /usr/src/app

# - Node uses a "package manager", so it needs to copy in package.json file
COPY package.json package.json

# - then it needs to run 'npm install' to install dependencies from that file
RUN npm install

# - to keep it clean and small, run 'npm cache clean --force' after above
RUN npm cache clean --force

# - then it needs to copy in all files from current directory
COPY . .

# - then it needs to start container with command '/sbin/tini -- node ./bin/www',
ENTRYPOINT ["/sbin/tini", "--"]
CMD [ "node", "./bin/www" ]
```

