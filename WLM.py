#!/usr/bin/env python3
import sys
with open("usage.txt", "r") as f:
	help = f.read()
if(len(sys.argv)<1):
	print("Python wordlist generator using personal information. See --help for usage.")
	sys.exit(1)
if(sys.argv[1] in ["--help", "-h"]):
	print(help)
	sys.exit(0)
if(len(sys.argv)<2):
	print("Python wordlist generator using personal information. See --help for usage.")
	sys.exit(1)
interactive = sys.argv[1] in ["--interactive", "-i"]
if(interactive and len(sys.argv)<3):
	print("Please provide an output file. See --help for usage.")
if(not interactive and sys.argv[1] not in ["--infile", "-f"]):
	print("%s: argument not understood"%sys.argv[1])
	sys.exit(1)
if(not interactive and len(sys.argv)<4):
	print("Please provide an output file. See --help for usage.")
	sys.exit(1)
outfile = sys.argv[-1]
if(not interactive):
	with open(sys.argv[2], "r") as f:
		answers = [i.strip() for i in f.readlines()]
else:
	answers = []
	with open("questions.txt", "r") as f:
		questions = [i.strip()+" " for i in f.readlines()]
	for i in questions:
		answers.append(input(i).strip())
