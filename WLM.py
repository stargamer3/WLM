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
	sys.exit(1)
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
name = answers[:4]
answers = answers[4:]
birthday = answers[0].split("/")
answers.pop(0)
keywords = answers[0].split(",")
answers.pop(0)
caps = answers[0].lower()=="y"
answers.pop(0)
numwords = int(answers[0]) if answers[0]!="" else 2
answers.pop(0)
numcharsb = int(answers[0]) if answers[0]!="" else 0
answers.pop(0)
numcharsa = int(answers[0]) if answers[0]!="" else 0
answers.pop(0)
letters = answers[0].lower()=="y"
digits = answers[0].lower()=="y"
others = answers[0].lower()=="y"
words = name+keywords
symbols = [i[0] for i in name]+birthday+[birthday[-1][:2]]+[birthday[-1][2:]]
if(letters):
	symbols+=list("abcdefghijklmnopqrstuvwxyz")
if(digits):
	symbols+=list("1234567890")
if(others):
	symbols+=list("!@#$%^&*()-_+=`~,./?><|{}[]\\")
