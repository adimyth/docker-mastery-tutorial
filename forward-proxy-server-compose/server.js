'use strict';

const express = require('express');

// constants
const PORT=80;
const HOST='0.0.0.0';

// application
const app = express();
app.get("/", (req, res) => {
	res.send("Hello World\n");
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);

