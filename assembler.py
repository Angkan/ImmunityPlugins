#!/usr/bin/env python

"""
	Name: assembler
	Usage: this plugin will generate opcode for me
  Helpful to make on the fly shellcode
	Author: n1ghtcr4wl3r
"""

__VERSION__='1.0'

#import libraries
import immlib
import immutils
import getopt
from immutils import *

#global hook to immunity debugger
imm = immlib.Debugger()

#Usage function
def usage():
	imm.log(" ** is this the usage?? ** ", focus=1, highlight=1)
	imm.log(" !assembler assemble <commands-to-assemble> [Note: segregate separate commands with #", focus=1, highlight=1)
	imm.log(" example: !assembler jmp esp#ret or pop#pop#ret", focus = 1, highlight=1)
	
#main function
def main(args):
	if len(args) == 0:
		usage()
	else:
		if args[0] == "assemble":
			cnt = 1
			getCommand = ""
			#below loop digests separate args and combines all args into one long string
			while cnt < len(args):
				getCommand = getCommand + args[cnt] + " "
				cnt = cnt+1
			getCommand = getCommand.split("#") #now we have a list of commands
			shellcode = ""
			for command in getCommand:
				try:
					assembled = imm.assemble(command)
					strAssembled = ""
					#further processing for a nicer display
					for assembCode in assembled:
						strAssembled = strAssembled + hex(ord(assembCode)).replace('0x','\\x')
					imm.log("command: %s ==> %s" %(command, strAssembled))
					shellcode = shellcode + strAssembled
				except:
					imm.log(" Could not assemble %s" %command, focus=1, highlight=1)
					continue
			imm.log("generated shellcode: %s" %shellcode)
		else:
			usage()
