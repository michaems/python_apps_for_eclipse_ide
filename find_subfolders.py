import os;

root = r"C:\Users\ett14478\Documents\nRF5_SDK"
pattern = ".h"

text_file = open("all_extracted.txt", "w");

dublicate_lines = set();

find_text = r"C:\Users\ett14478\Documents\nRF5_SDK\nRF5_SDK_17_1_0_ddde560"
replace_text = r"$(SDK_ROOT)"

exclude = {"examples", "s113", "s340", "s132", "s212", "s312", "s332", "pca10040", "pca10100", 
           "pca10100e", "pca10056e", "52810", "52811", "52820", "52832", "52833"}

def check_is_not_excluded(folder_name):
    return_value = 0;
    for excl in exclude:
        if excl in folder_name:
            return_value = 1
    
    return return_value      



for path, subdirs, files in os.walk(root):
    for name in files:
        if name.endswith(pattern):
            dirname = os.path.dirname(path)
            dirname = dirname.replace(find_text, replace_text)
            if dirname not in dublicate_lines:
                if check_is_not_excluded(dirname) == 0:
                    text_file.write(dirname + "\r")
                    dublicate_lines.add(dirname)
                    print(os.path.join(path, name))
                


    
