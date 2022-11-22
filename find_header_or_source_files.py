import os;

#find file and print the folder into .txt file

root = r"C:\Users\ett14478\Documents\nRF5_SDK"

file_to_find = {"nrfx_glue.h", "arduino_primo.h"}

text_file = open("files_found_in_subfolders.txt", "w")

find_text = r"C:\Users\ett14478\Documents\nRF5_SDK\nRF5_SDK_17_1_0_ddde560"
replace_text = r"$(SDK_ROOT)"

for path, subdirs, files in os.walk(root):
    for name in files:
        if name in file_to_find:
            dirname = path
            dirname = dirname.replace(find_text, replace_text)
            text_file.write(dirname + "\r")
            print(os.path.join(path, name))