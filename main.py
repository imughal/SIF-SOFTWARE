#!/usr/bin/python
# Importing
import xmlClass
from rgfun import *
from xmlExpClass import *

#Global Links
DATAFILE = "employees.xml"


newPrint = xmlClass.xmlDataBase(DATAFILE)
empData = newPrint.dataImp()
for i in empData:
    newa = [i.name, i.iban, i.basic, i.lcard, i.company, i.brno, i.cocode]
    for k in newa:
        print k
    br()
xmlExport(DATAFILE,empData)
