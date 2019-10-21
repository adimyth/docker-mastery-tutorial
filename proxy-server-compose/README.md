# Sample Docker Node App

A dockerized version of "Hello World" node app

## Creating a node app
1. package.json

Adding `Express` framework as an essential node dependencies. 
```
{
	"name": "hello-world-node-app",
	"version": "1.0.0",
	"description": "Hello World Node app",
	"author": "Aditya Mishra <mishraaditya6991@gmail.com",
	"main": "server.js",
	"scripts": {
		"start": "node server.js"
	},
	"dependencies": {
		"express": "^4.16.1"
	}
}
```
Run `npm install`

2. server.js

Application to create a simple HTTP server that will serve our "Hello World" website on `localhost:8080`
```
'use strict';

const express = require('express');

// constants
const PORT=8080;
const HOST='0.0.0.0';

// application
const app = express();
app.get("/", (req, res) => {
	res.send("Hello World\n");
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
```
Run `node server.js` & check `localhost:8080` in your web browser, it should display "Hello World" message

## Docker container

1. Creating an image

This will be our app & contains all the essentials.
```
# install the latest node version
FROM node

# setting working directory 
WORKDIR /usr/src/app

# copy files
COPY . .

# install node dependencies
RUN npm install

# listen on port 8080
EXPOSE 8080

# run node server
CMD ["node", "server.js"]
```
2. Building the image

Build a docker image using the above Dockerfile & name it `node-app`
```
docker image build -t node-app .
```
3. Running the container

```
docker container run -p 80:8080 -d --name "hello-world-node-app" node-app
```
4. Testing the app
```
curl localhost
```
