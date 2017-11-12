#!/usr/bin/env python

"""
	Name: searchCmd
	Usage: find whatever command(s) you may like in a process memory
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
	imm.log(" !searchCmd <command-to-search> [Note: separate spaces in command with # and append other commands with \\n]", focus=1, highlight=1)
	imm.log(" example: !searchcmd jmp#esp@ret or pop@pop@ret", focus = 1, highlight=1)
	
#main function
def main(args):
	if len(args) == 0:
		usage()
	else:
		imm.log("usage is correct")
		searchFor = args[0]
		searchFor = searchFor.replace("#"," ").replace("@","\n")
#		imm.log("supplied argument is: %s" %searchFor)
		imm.updateLog()
		results = imm.search(imm.assemble(searchFor))
		if not results:
			imm.log(" ** well! I couldn't find any!! **",focus=1,highlight=1)
		for result in results:
			imm.log("Found %s at 0x%08x" %(searchFor.replace('\n','-'),result), address=result, focus=1, highlight=1)
		
