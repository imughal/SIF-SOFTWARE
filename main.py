#!/usr/bin/python
# Importing
import xmlClass
from rgfun import *

# new


newPrint = xmlClass.xmlDataBase("employees.xml")
empData = newPrint.dataImp()
for i in empData:
<<<<<<< HEAD
    newa = [i.name, i.iban, i.basic, i.lcard, i.company, i.brno, i.cocode]
    print newa[2]
=======
    newa = [i.name,i.iban,i.basic,i.lcard,i.company,i.brno,i.cocode]
    for k in newa:
        print k
>>>>>>> b399baebb0282fee57a6adc37fb10a374149cbae
    br()
