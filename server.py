from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
import SocketServer

PORT = 9872
httpd = SocketServer.TCPServer(("", PORT), Handler)

print ("Serving at port %d" % (PORT,))
httpd.serve_forever()


