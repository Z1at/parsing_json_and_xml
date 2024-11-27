import xml.etree.ElementTree as ET


tree = ET.parse("task_xml.xml")

root = tree.getroot()
# print(root.tag)
# print(len(root))
#
# print(root[0].attrib)
# print(len(root[0]))
# print(root[0][0].attrib)

for i in range(len(root)):
    print(root[i].tag)
    for j in root[i].attrib:
        print(j + ":", root[i].attrib[j])
    if len(root[i]):
        print("attributes:")
        for j in range(len(root[i])):
            print("\tname:", root[i][j].attrib["name"])
            print("\ttype:", root[i][j].attrib["type"])
            print()
    if root[i].text:
        print("text:", root[i].text.strip())
    print()
