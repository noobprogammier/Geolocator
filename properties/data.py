from json import loads, dumps
class exception(Exception):
	inits = {}
	inits["JSON-ERROR"] = ["JSON-ERROR", "Item is not found in the dict!"]
class SendandReceive(exception):
	def JSONMode(self):
		rma = loads(("".join(self.sock.recv(124821).decode("utf-8", errors="ignore") for _ in range(1))).split("\r\x0A\r\x0A")[1].strip())
		if self.go not in rma and self.go != "keyall":
			raise exception(exception.inits["JSON-ERROR"][1])
		if self.go == "keyall":
			self.output = rma
		else:	
			self.output = {"target":rma[self.go]}
	def __init__(self, output):
		header = "GET /json/%s HTTP/1.1\r\x0AHost: www.ip-api.com\r\x0AConnection: close\r\x0AUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36\r\x0AAccept: */*\r\x0A\r\x0A"%(self.ipaddr)
		self.sock.send(header.encode("utf-8", errors="ignore"))
		caser = {"JSON":SendandReceive.JSONMode}[output]
		caser(self)