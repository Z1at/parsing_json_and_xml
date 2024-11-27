from xml.etree import ElementTree as ET


def pretty_xml(element, indent, newline, level=0):  # elemnt is the Elment class passed in, the parameter indent is used for indentation, and newline is used for line break
    if element:  # Determine whether the element has child elements
        if (element.text is None) or element.text.isspace():  # If the element text has no content
            element.text = newline + indent * (level + 1)
        else:
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
    # else: # If you remove the comment on the two lines here, the element text will also start a new line
    #     element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * level
    temp = list(element)  # convert element to list
    for subelement in temp:
        if temp.index(subelement) < (len(temp) - 1):  # If it is not the last element of the list, it means that the next line is the beginning of the element at the same level, and the indentation should be the same
            subelement.tail = newline + indent * (level + 1)
        else:  # If it is the last element of the list, it means that the next line is the end of the parent element, and the indentation should be one less
            subelement.tail = newline + indent * level
        pretty_xml(subelement, indent, newline, level=level + 1)  # Perform recursive operations on sub-elements


root = ET.Element("student")

first_name = ET.SubElement(root, "firstName")
first_name.text = "Greg"

second_name = ET.SubElement(root, "secondName")
second_name.text = "Dean"

scores = ET.SubElement(root, "scores")

module1 = ET.SubElement(scores, "module1")
module1.text = "100"

module2 = ET.SubElement(scores, "module2")
module2.text = "80"

module3 = ET.SubElement(scores, "module3")
module3.text = "90"

tree = ET.ElementTree(root)
pretty_xml(root, "\t", "\n")
tree.write("save_xml.xml")


