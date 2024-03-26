import os
import re

directory = "D:\OneDrive - UMH\Manuscritos\Revisión\Germoplasmas"

files_list = os.listdir(directory)

total_count = 0

file_germplasm = open(directory + "\\" + "germplasm.txt", "w")

for element in files_list:
    element_path = directory + "\\" + element
    file = open(element_path, "r")

    count = 0

    for line in file:
        id = re.search(r"id=(\d+)&type=germplasm", line)
        if id:
            count += 1
            file_germplasm.write(id.group(1) + "\n")

    print(element + ": " + str(count))
    total_count += count
    
    file.close()

file_germplasm.close()
print("Number of germplasms found: " + str(total_count))
