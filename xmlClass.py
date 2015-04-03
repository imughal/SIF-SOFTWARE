#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom
import empClass
from rgfun import *

class xmlDataBase(object):
	
	
	def __init__(self,xmlFile):
		self.DOMTree = xml.dom.minidom.parse(xmlFile)
		self.collection = self.DOMTree.documentElement

	def data(self,dataList):

		self.collection.getAttribute("company")
		self.collection.getAttribute("brno")

		employees = self.collection.getElementsByTagName("employee")
		for employee in employees:
			newemp = empClass.xEmployee(employee.getAttribute("name"))
			newemp.company=self.collection.getAttribute("company")
			newemp.brno=self.collection.getAttribute("brno")
			newemp.cocode=self.collection.getAttribute("cocode")
			#print "***EMPLOYEE***"
			#if employee.hasAttribute("name"):
				#print employee.getAttribute("name")
				#print employee.getAttribute("company")
			
			newemp.iban = employee.getElementsByTagName('IBAN')[0].childNodes[0].data
			newemp.lcard = employee.getElementsByTagName('lcard')[0].childNodes[0].data
			newemp.basic = employee.getElementsByTagName('basic')[0].childNodes[0].data
			
			#print "iban:",newemp.iban
			#print "lcard:",newemp.lcard
			#print "basic:",newemp.basic
			
			dataList.append(newemp)
			
			
dataemp = []
newPrint = xmlDataBase("employees.xml")
newPrint.data(dataemp)
for i in dataemp:
	print i.name
	print i.iban
	print i.basic
	print i.lcard
	print i.company
	print i.brno
	print i.cocode
	br()
