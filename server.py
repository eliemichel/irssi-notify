#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from subprocess import call

PORT = 9871
# The notif command should expect 2 arguments. If it does not, you just
# have to change a single line bellow. (see comments)
NOTIF_COMMAND = 'notify-send'

def notif_filter(q):
	conditions = [
		'info' in q,
		# This is an example of blacklisting
		# (each message from pfcbot will be ignored)
		'- Nouveau message de pfcbot -' not in q['info']
	]
	
	return all(conditions)

def notif_escape(msg):
	return msg.replace('\\', '\\\\')


class Handler(BaseHTTPRequestHandler):
	def do_GET(s):
		req = urlparse(s.path)
		q = parse_qs(req.query)
		
		if req.path == '/notify':
			if notif_filter(q):
				# If your notify command expect more or less than 2
				# arguments, please edit the next line.
				call([NOTIF_COMMAND, 'IRC', notif_escape(q['info'][0])])
			else:
				print("Muted request")
		
		s.send_response(200)
		s.end_headers()


def main():
	httpd = HTTPServer(('localhost', PORT), Handler)
	print("Serving at port %d" % (PORT,))
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
	print("\nServer closed")


if __name__ == '__main__':
	main()


