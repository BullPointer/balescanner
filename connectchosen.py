#!/usr/bin/python3

from socket import *
from termcolor import colored

def connectChosenScan(tgthost, tgtport):
	sock = socket(AF_INET, SOCK_STREAM)
	try:
		sock.connect((tgthost, tgtport))
		print(colored("{}/tcp   open".format(tgtport), "blue"))
	except:
		print(colored("{}/tcp   close".format(tgtport), "red"))
	finally:
		sock.close()
