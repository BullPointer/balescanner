#!/usr/bin/python3

from socket import *
from termcolor import colored

def connectAllScan(tgthost, tgtport):
	sock = socket(AF_INET, SOCK_STREAM)
	try:
		sock.connect((tgthost, tgtport))
		print(colored("{}/tcp   open".format(tgtport), "blue"))
	except:
		pass
	finally:
		sock.close()
