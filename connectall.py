#!/usr/bin/python3

import os
from socket import *
from termcolor import colored

def connectAllScan(tgthost, tgtports):
	sock = socket(AF_INET, SOCK_STREAM)
	try:
		sock.connect((tgthost, tgtports))
		print(colored("{}/tcp   open".format(tgtports), "blue"))
	except:
		pass
	finally:
		sock.close()
		
