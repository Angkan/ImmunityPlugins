#!/usr/bin/env python

"""
	Name: popopret
	Usage: find pop-pop-ret instruction for seh based overflows
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
	imm.log(" !popopret <command-to-search> [Note: separate spaces in command with # and append other commands with \\n]", focus=1, highlight=1)
	imm.log(" example: !searchcmd jmp#esp@ret or pop@pop@ret", focus = 1, highlight=1)
def main(args):
	if len(args) == 0:
		usage()
	else:
		imm.log("usage is correct")
		searchFor = args[0]
		searchFor = searchFor.replace("#"," ")
		imm.log("supplied argument is: %s" %searchFor)
		imm.updateLog()
		results = imm.search(imm.assemble(searchFor))
		for result in results:
			imm.log("Found %s at 0x%08x" %(searchFor,result), address=result, focus=1, highlight=1)
		
