"""
This tool is for IP lookup, geolocation information of the IP address.
---------
This tool is manufactured by sipistoverdi organization, specifically to find IP geolocation and to find the correct time zone, in order to put the correct hour
in the header.
It uses ip-api.com as an external database.
-------------------------------------------
"""
from properties.socketc_ import socketc
from properties.data import SendandReceive
from time import time
class GetIPLoc(socketc, SendandReceive):
	def __init__(self, ip_address="0.0.0.0", get_only="timezone", output="JSON", help_=None):
		if help_ != None:
			print("HELP Module for JSON serialization. . .\x0A" + "\x2D"*40 + "\x0AKey1: status\x0AKey2: country\x0AKey3: countryCode\x0AKey4: region\x0AKey5: regionName\x0AKey6: city\x0AKey7: zip\x0AKey8: lat\x0AKey9: lon\x0AKey10: timezone\x0AKey11: isp\x0AKey12: org\x0AKey13: as\x0AKey14: query\x0A\x0AAdditional: Type 'keyall' to get all keys and values\x0A\x0A" + "\x2D"*40)
			exit()
		self.ipaddr = ip_address
		self.go = get_only
		self.start_ = time()
		socketc.__init__(self)
		SendandReceive.__init__(self, output)
		self.end_ = time()
	@property
	def getInfo(self):
		self.output["time-finished"] = str(abs(int((self.start_ - self.end_)*1000))) + " ms"
		return self.output
if __name__ == "__main__":
	rout = GetIPLoc(ip_address="85.130.18.91", get_only="country").getInfo
	print(rout)