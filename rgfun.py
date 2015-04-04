#!/usr/bin/python
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
			break
		except:
			print "Invalid Input"
	return new_int
#still not figured out how to comlete it.

def check_inp(inp,x):
	if x == "Year":
		
		pass
#still not figured out how to comlete it.

if __name__ == "__main__":
	print "Error-Invalid File to Run- Please Run main.py."
