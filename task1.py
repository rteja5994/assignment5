import math

class Network_Subnetting:

	def __init__(self,ip,prefix):
		self.net_address = []
		self.prefix = []
		ip = ip.split(".")
		ad = "1"*prefix + "0"*[32-prefix]
		octet = (ad[0:8],ad[8:16],ad[16:24],ad[24:32])

	
	for p in range(len(ip)):
                a = int(ip[p])
                b = int(octet[p], 2)
                self.net_addr.append(a&b)	
