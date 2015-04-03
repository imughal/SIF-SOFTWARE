#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom

class xmlDataBase(Object):
	
	
	def __init__(self,xmlFile)
	self.DOMTree = xml.dom.minidom.parse(xmlFile)
	self.collection = self.DOMTree.documentElement

	def

	if collection.hasAttribute("company"):
		print "Root Element: %s" % collection.getAttribute("company")
		print collection.getAttribute("brno")

	employees = collection.getElementsByTagName("employee")
	for employee in employees:
		print "***EMPLOYEE***"
		if employee.hasAttribute("name"):
			print employee.getAttribute("name")
			print employee.getAttribute("company")
		
		iban = employee.getElementsByTagName('IBAN')[0].childNodes[0].data
		lcard = employee.getElementsByTagName('lcard')[0].childNodes[0].data
		basic = employee.getElementsByTagName('basic')[0].childNodes[0].data
		
		print "iban:",iban
		print "lcard:",lcard
		print "basic:",basic

