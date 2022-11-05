#!/usr/bin/python3

from socket import *
from threading import *
from connectchosen import connectChosenScan
from connectall import connectAllScan


def  portrequest(tgthost, tgtports, tgtallports):
	try:
		ipAddr = gethostbyname(tgthost)
	except:
		print(f"Unknown request for {tgthost} or Check your internet connection")
	try:
		domainName = gethostbyaddr(ipAddr)
		print("Scaning for {}".format(domainName[0]))
		print("PORT STATE")
	except:
		print("Scanning for {}".format(ipAddr))
		print("PORT  STATE")
	setdefaulttimeout(1)
	try:
		if (tgthost != None) and (tgtallports == None) and (tgtports[0] == 'None'):
			for tgtport in range(1, 1000):
				thread = Thread(target=connectAllScan, args=(tgthost, int(tgtport)))
				thread.start()
		elif (tgtallports == None):
			for tgtport in tgtports:
				thread = Thread(target=connectChosenScan, args=(tgthost, int(tgtport)))
				thread.start()
		else:
			for tgtport in range(1, 65536):
				thread = Thread(target=connectAllScan, args=(tgthost, int(tgtport)))
				thread.start()
	except:
		print("Oops! Please check you host input and internet connection or read Assist for program. Thank you...")
		exit()
			
