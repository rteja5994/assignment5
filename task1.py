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
                self.net_address.append(a&b)	

	print ("Network Address:", self.net_addr)

	def subnet(self,count):
		c = int(math.log(count,2))
		tar = self.prefix + c
		ad = "1"*tar + "0"*[32-tar]
		octet = (ad[0:8],ad[8:16],ad[16:24],ad[24:32])
		print (octet)

		move = math.ceil( target / 8.0 ) #steps to identify which octets needs to be moved
        	host = (move*8) - target

		jump = 2**host #to identify the interval


		
		
