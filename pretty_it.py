#!/usr/bin/python3

import sys
from bs4 import BeautifulSoup

the_xml_files = sys.argv[1:] or ['rc.xml', 'menu.xml']

for the_xml_file in the_xml_files:

    bs = BeautifulSoup(open(the_xml_file), 'xml')
    the_pretty_xml = bs.prettify()
    with open(the_xml_file, 'w') as fob:
        fob.write(the_pretty_xml)


