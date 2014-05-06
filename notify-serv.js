#!/usr/bin/env node

var NOTIF_COMMAND = 'notify-send';

var express = require('express'),
    spawn = require('child_process').spawn;


function filter(msg) {
	return (
		nick != 'pfcbot' &&
		nick != 'Eve'
	)
}



express()
.use(express.bodyParser())
.post('/notify', function (req, res) {
	console.log('Request for ' + req.body.nick + ', ' + req.body.msg + ', ' + req.body.chan);
	msg = req.body.msg.replace("\\", "\\\\");
	chan = req.body.chan.replace("\\", "\\\\");
	nick = req.body.nick.replace("\\", "\\\\");
	if (filter(nick)) {
		spawn(NOTIF_COMMAND, ['IRC - ' + (chan != '' ? nick + ' sur ' + chan : 'Message privé de ' + nick), msg]);
	}
	else {
		console.log('[muted]');
	}
	res.statusCode = 200;
	res.end('');
})
.listen(9871);

console.log('Serveur lancé');

