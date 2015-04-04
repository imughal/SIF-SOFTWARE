#!/usr/bin/python
#Importing
import xmlClass
from rgfun import *

#new
newPrint = xmlClass.xmlDataBase("employees.xml")
empData = newPrint.dataImp()
for i in empData:
	newa = [i.name,i.iban,i.basic,i.lcard,i.company,i.brno,i.cocode]
	print newa[2]
	br()
