#!/usr/bin/env nodejs

var express = require('express'),
    spawn = require('child_process').spawn;

express()
.get('/notify', function (req, res) {
	console.log('Request for ' + req.query.info);
	msg = req.query.info.replace("\\", "\\\\");
	spawn('notify-send', ['IRC', msg]);
	res.statusCode = 200;
	res.end('');
})
.listen(9871);

console.log('Serveur lancé');

