#!/usr/bin/env node

var express = require('express'),
    spawn = require('child_process').spawn;

express()
.use(express.bodyParser())
.post('/notify', function (req, res) {

    nick = req.body.nick;
    chan = req.body.chan;
    msg = req.body.msg;
    console.log(chan + " <" + nick + "> " + msg);

	msg = msg.replace("\\", "\\\\");
	chan = chan.replace("\\", "\\\\");
	nick = nick.replace("\\", "\\\\");
    if (nick != "pfcbot" && nick != "pfcplayer") {
    	spawn('notify-send', ["<" + nick + "> " + chan, msg]);
    }

	res.statusCode = 200;
	res.end('');
})
.listen(9871);

console.log('Serveur lancé');

