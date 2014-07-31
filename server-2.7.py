import BaseHTTPServer
from urllib import unquote_plus
from subprocess import call

import config
HOST_NAME = vars(config)['HOST_NAME']
PORT_NUMBER = vars(config)['PORT_NUMBER']

class NotifyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s): print 'HEAD request can\'t be answered.'
    def do_GET(s): print 'GET request can\'t be answered.'

    def do_POST(s):
        # Change this if you want to change the way the data
        # are extracted :
        data = {}
        for e in s.rfile.read().split('&'):
            data[e.split('=')[0]] = unquote_plus(e.split('=')[1])

        # Change this if you want to change the way the data
        # are used (or not) :
        if data['nick'] in ['Eve', 'nsfbot']:
            return False

        # Change this if you want to change the way you're
        # being notified :
        call(['notify-send',
              '-i', '/home/niols/irssi-notify/irssi.png',
              '%s on %s'%(data['nick'],data['chan']),
              data['msg']])

        return True

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), NotifyHandler)
    print 'Server Starting on %s:%s'%(HOST_NAME,PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print 'Server Stoped'
