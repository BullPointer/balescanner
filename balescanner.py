#!/usr/bin/python3

from socket import *
import optparse
from portreq import portrequest


def main():
	parser = optparse.OptionParser("Use Assist for program: " + "[-P0 *Scan all target open Ports*] [-p *scan targeted port*] {-H *target Host specification*}")
	parser.add_option("-P", dest="tgtallport", type="string", help="Scan all open ports")
	parser.add_option("-p", dest="tgtport", type="string", help="Specify port or ports, seperated by comma")
	parser.add_option("-H", dest="tgthost", type="string", help="Specify Host to scan")
	(options, args) = parser.parse_args()
	tgtallports = options.tgtallport
	tgtports = str(options.tgtport).split(",")
	tgthost = options.tgthost
	if (tgthost == None):
		print("Kindly set a host *required")
		print(parser.usage)
		exit(0)
	elif (options.tgtport != None) and (options.tgtallport != None):
		print("""Hey there! Do you want to scan specific port or do you want to scan all?
This should help: {}		
		""".format(parser.usage))
		exit(0)
	print("You are good to go")

	portrequest(tgthost, tgtports, tgtallports)
	
if __name__ == "__main__":
	main()
	
	
