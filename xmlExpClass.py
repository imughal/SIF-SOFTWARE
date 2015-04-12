import xml.etree.cElementTree as ET

def xmlExport(fileName,Elist):
	
	root = ET.Element("employees",company=Elist[0].company, brno=Elist[0].brno, cocode=Elist[0].cocode)
	for k in Elist:	
		doc = ET.SubElement(root, "employee", name = k.name)
	
		ET.SubElement(doc, "fullname").text = k.fullname
		ET.SubElement(doc, "IBAN").text = k.iban
		ET.SubElement(doc, "lcard").text = k.lcard
		ET.SubElement(doc, "basic").text = k.basic


	tree = ET.ElementTree(root)
	tree.write(fileName)
