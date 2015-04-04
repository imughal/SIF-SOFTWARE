#!/usr/bin/python
#Importing
import xmlClass
from rgfun import *

#new
newPrint = xmlClass.xmlDataBase("employees.xml")
empData = newPrint.dataImp()
for i in empData:
	print i.name
	print i.iban
	print i.basic
	print i.lcard
	print i.company
	print i.brno
	print i.cocode
	br()
