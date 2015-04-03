#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("employees.xml")
collection = DOMTree.documentElement

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

