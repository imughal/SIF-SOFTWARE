#!/usr/bin/python
from datetime import date

def br():
	print ""
	
def stline():
	print "------------------------"

def waits():
	try:
		n = 1
		while n<(9999 * 999):
			n += 1
	except:
		print "print Error"

def get_int(message,x=""):
	while True:
		try:
			new_int=int(raw_input(message))
			if check_inp(new_int,x):
				break
		except:
			print "Invalid Input"
	return new_int
	
#still not figured out how to complete this.

def check_inp(inp,x):
	if x == "year":
		if inp <=2000 or inp > date.today().year:
			print "Error, Wrong Year"
			return False
		else:
			return True
	elif x == "day":
		if inp <= 0 or inp > 31:
			print "Error, Wrong Year"
			return False
		else:
			return True	
	elif x == "month":
		if inp <= 0 or inp > 12:
			print "Error, Wrong Year"
			return False
		else:
			return True
			
#still not figured out how to comlete it.

if __name__ == "__main__":
	print "Error, Cannot Execute"
