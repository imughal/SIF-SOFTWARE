#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("employees.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("company"):
	print "Root Element: %s" % collection.getAttribute("company")

employees = collection.getElementsByTagName("employee")
for employee in employees:
	print "***EMPLOYEE***"
	if employee.hasAttribute("name"):
		print employee.getAttribute("name")
		
	type = employee.getElementsByTagName('type')[0]
	print "Type: %s" % type.childNodes[0].data
	format = employee.getElementsByTagName('format')[0]
	print "format: %s" % format.childNodes[0].data
	rating = employee.getElementsByTagName('rating')[0]
	print "rating: %s" % rating.childNodes[0].data
	description = employee.getElementsByTagName('description')[0]
	print "description: %s" % description.childNodes[0].data