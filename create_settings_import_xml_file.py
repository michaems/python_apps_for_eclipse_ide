from xml.dom import minidom
import xml.etree.ElementTree as gfg 
import os

text_file_name = r"all_extracted.txt"

text_file = open(text_file_name, "r")

root = minidom.Document();
root.version="1.0"

xml = root.createElement('cdtprojectproperties')
root.appendChild(xml)

section = root.createElement("section")
section.setAttribute('name', 'org.eclipse.cdt.internal.ui.wizards.settingswizards.IncludePaths')

lang1 = root.createElement("language");
lang1.setAttribute("id", "org.eclipse.cdt.core.gcc");
lang1.setAttribute("name", "C Source File");

lang2 = root.createElement("language");
lang2.setAttribute("id", "org.eclipse.cdt.core.assembly");
lang2.setAttribute("name", "Assembly Source File");

lang3 = root.createElement("language");
lang3.setAttribute("id", "org.eclipse.cdt.core.g++");
lang3.setAttribute("name", "C++ Source File");

for path in text_file:
    include_path1 = root.createElement("includepath");
    include_path1.appendChild(root.createTextNode(path.strip()))
    include_path2 = root.createElement("includepath");
    include_path2.appendChild(root.createTextNode(path.strip()))
    include_path3 = root.createElement("includepath");
    include_path3.appendChild(root.createTextNode(path.strip()))
    lang1.appendChild(include_path1);
    lang2.appendChild(include_path2);
    lang3.appendChild(include_path3);
    

  

section.appendChild(lang1);
section.appendChild(lang2);
section.appendChild(lang3);

xml.appendChild(section)

xml_str = root.toprettyxml()

save_path_file = "ready_to_be_imported.xml"

with open(save_path_file, "w") as f:
	f.write(xml_str)
