#!/usr/bin/env python

"""
	Name: readmem
	Usage: To learn how to step through memoryview
	Author: n1ghtcr4wl3r
"""

__VERSION__='1.0'
#importing necessary modules
import immlib
import immutils
import getopt
from immutils import *

#global debugger hook
imm = immlib.Debugger()

#usage function
def usage():
	imm.log(" ** is this the usage?",focus=1, highlight=1)
	imm.log("Usage: !readmem read <addr_in_hex>")
	
#main function
def main(args):
	if not args:
		usage()
	else:	
		if (args[0]=="read"):
			if (len(args) > 1):
				imm.log("Reading 8 bytes of memory at %s" %args[1])
				cnt = 0
				memloc = int(args[1],16)
				while cnt < 8:
					memchar = imm.readMemory(memloc+cnt,1)
					memchar2 = hex(ord(memchar)).replace('0x','')
					imm.log("Byte %d: %s" %(cnt+1,memchar2))
					cnt = cnt+1
			else:
				usage()
		else:
			usage()
