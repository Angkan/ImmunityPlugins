#!/usr/bin/env python

"""
	Name: readreg.py
	Usage: To read the curent register values
	Author: n1ghtcr4wl3r
"""

__VERSION__='1.0'
#importing libraries
import immlib
import immutils
import getopt
from immutils import *

#immunity global hook
imm = immlib.Debugger()

#main function
def main():
#	regs = imm.getRegs()
#	for reg in regs:
#		imm.log("Register %s: 0x%08X" %(reg, regs[reg]))
	imm.log("hello")
