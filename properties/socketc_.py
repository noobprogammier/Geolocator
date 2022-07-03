from socket import socket, AF_INET, SOCK_STREAM, getprotobyname
class socketc(object):
	def __init__(self):
		self.sock = socket(AF_INET, SOCK_STREAM, getprotobyname("tcp"))
		self.sock.connect(("www.ip-api.com", 80))