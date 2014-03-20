#!/usr/bin/env nodejs

var express = require('express'),
    spawn = require('child_process').spawn;


function filter(msg) {
	return (msg.match('- Nouveau message de pfcbot -') == null)
}



express()
.get('/notify', function (req, res) {
	console.log('Request for ' + req.query.info);
	msg = req.query.info.replace("\\", "\\\\");
	if (filter(msg)) {
		spawn('notify-send', ['IRC', msg]);
	}
	else {
		console.log('muted');
	}
	res.statusCode = 200;
	res.end('');
})
.listen(9871);

console.log('Serveur lancé');

