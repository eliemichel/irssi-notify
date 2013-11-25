var express = require('express'),
    spawn = require('child_process').spawn;

express()
.get('/notify', function (req, res) {
	console.log('Request for ' + req.query.info);
	spawn('notify-send', ['IRC', req.query.info]);
	res.statusCode = 200;
	res.end('');
})
.listen(9871);

console.log('Serveur lancé');

