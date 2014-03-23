# Irssi-Notify #

Notifications for the IRC client [Irssi](http://www.irssi.org/) *via* a simple http server.

We use a http server for the notfication system to work over an ssh connexion for exemple (cf *Usage* section).

The system is divided into two parts : the script for Irssi which fires http requests and the server that handle them and call a given command.

Two versions of the server are available. The first one uses [nodejs](http://nodejs.org/) and the second one is made with Python 3.

The command called by default is `notify-send` but it can easily be replaced by changing the value of `NOTIF_COMMAND` in server.py or notify-serv.js.


## Usage ##

For both servers the begining is the same :

1. Put notify.pl in `~/.irssi/scripts`
2. Type `/script load notify` in Irssi

Then you have to choose the server system you prefere :

### With Nodejs

1. Install required node packages with `npm install`
2. Start the notify server : `./notify-server.js` or `node notify-server.js`


### With Python

1. Run `./server.py` or `python3 server.py`

**Note**: If you can't run the server (`./notify-server.js : command not found` or `./server.py : command not found`), try to make the file executable with `chmod +x notify-server.js` or `chmod +x server.py` respectively.


### Over SSH

If you use Irssi over ssh, you just have to forward port 9871 when you connect
to ssh, like this :

    ssh user@host -R 9871:localhost:9871



## Customization ##

If you want use your own script to handle notifications instead of the default
`notify-send`, just replace it in notify-server.js or server.py.

You can for example use the `beep` command to repalce visual notifications by a sound.

You can also change the format of the notifications in the notify.pl irssi script. (For example to translate it from French…)

## LICENCE ##

The MIT License (MIT)

Copyright (c) 2013 - 2014 Elie Michel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

