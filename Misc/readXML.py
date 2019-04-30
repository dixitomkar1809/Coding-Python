# Author: Omkar Dixit
# Email: ond170030@utdallas.edu

# Read XML

import xml.etree.ElementTree as ET
from xml.dom import minidom

tree = ET.parse('temp.xml')
root = tree.getroot()
for child in root:
    print("{}: {}".format(child.tag, child.attrib))
xmldoc = minidom.parse('temp.xml')
itemList = xmldoc.getElementsByTagName('country')
for i in itemList:
    # print(i)
    print(i.attributes['name'].value)