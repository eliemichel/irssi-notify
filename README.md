# Irssi-Notify #

Notifications for [Irssi](http://www.irssi.org/) *via* a simple http server.

Requires [nodejs](http://nodejs.org/) for the server and the `notify-send` command (but it can easily be replaced).


## Usage ##

1. Start the notify server : `./notify-server`
2. Put notify.pl in `~/.irssi/`
3. Type `/script load notify` in Irssi

Note: If you can't run the server (`./notify-server : command not found`), try
to make the file executable with `chmod +x notify-server`.

If you use Irssi over ssh, you just have to forward port 9871 when you connect
to ssh, like this :

    ssh user@host -R 9871:localhost:9871



## Customization ##
If you want use your own script to handle notifications instead of the default
`notify-send`, just replace it in notify-server.js


## LICENCE ##

The MIT License (MIT)

Copyright (c) 2013 Elie Michel

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

