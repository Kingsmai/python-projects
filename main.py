import xml.etree.ElementTree as ET
import re

with open("Data/sk_playerprefs_v2.xml", 'r', encoding="utf-8") as file_lines:
    xml_string = ""
    for line in file_lines:
        xml_string += line

tree = ET.ElementTree(ET.fromstring(xml_string))
root = tree.getroot()

root = ET.fromstring(xml_string)

# Sort
# root[:] = sorted(root, key=lambda child: (child.tag, child.get('name')))

for child in root.iter('int'):
    if re.match(r"c\d+_skin\d+", child.get("name")):
        print(child.get("name"))
        child.set("value", "1")
    if child.get("name") == "gems" and child.get("name") == "var_gems" and child.get("name") == "last_gems":
        child.set("value", "99999999")
    if re.match(r"c_\w+_skill_\d+_unlock", child.get("name")):
        child.set("value", "1")

for child in root.iter('string'):
    if re.match(r"c\d+_unlock", child.get("name")):
        child.text = "true"
    # if re.match(r"p\d+_unlock", child.get("name")):
    #     child.text = "true"

# tree.write("Output/sk_playerprefs_v2.xml", encoding="utf-8")

xmlstr = ET.tostring(root, encoding="utf-8", method="xml")
#
with open("Output/sk_playerprefs_v2.xml", 'w', encoding="utf-8") as new_file:
    new_file.write("<?xml version='1.0' encoding='utf-8' standalone='yes' ?>\n")
    new_file.write(xmlstr.decode("utf-8"))
