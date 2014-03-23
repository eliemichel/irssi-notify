#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from subprocess import call

PORT = 9871


def notif_filter(q):
	return \
		'info' in q and \
		'- Nouveau message de pfcbot -' not in q['info']

def notif_escape(msg):
	return msg.replace('\\', '\\\\')


class Handler(BaseHTTPRequestHandler):
	def do_GET(s):
		req = urlparse(s.path)
		q = parse_qs(req.query)
		print(req.path)
		if req.path == '/notify':
			if notif_filter(q):
				call(['notify-send', 'IRC', notif_escape(q['info'][0])])
			else:
				print("Muted request")
		s.send_response(200)
		s.send_header("Content-type", "text/plain")
		s.end_headers()
		print()


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


