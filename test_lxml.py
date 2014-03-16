import lxml
from lxml import etree

some_xml = "<root>data</root>"
root = etree.fromstring(some_xml)
print root.tag
