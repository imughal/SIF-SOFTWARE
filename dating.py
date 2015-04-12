#!/usr/bin/python

class Dating(object):
	monthDaysA=[["JANUARY",31],["FEBRUARY",28],["FEBRUARYL",29],["MARCH",31],["APRIL",30],["MAY",31],["JUNE",30],["JULY",31],["AUGUST",31],["SEPTMBER",30],["OCTOBER",31],["NOVEMBER",30],["DECEMBER",31]]
	
	
	def __init__(self):
		self.self = self
		
	def monthDays(self,month):
		for x in self.monthDaysA:
			if x[0] == month:
				return x[1]
		
		
x = Dating()

print x.monthDays("FEBRUARYL")
