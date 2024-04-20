from urllib.request import urlopen
import time

file_germplasm_list = open("germplasm_refined_18.txt", "r")

germplasm_codes = file_germplasm_list.readlines()

file_length = len(germplasm_codes)
count = 1
errors = []

for code in germplasm_codes:
    try:
        clean_code = code.rstrip()

        page = urlopen("https://www.arabidopsis.org/servlets/TairObject?id=" + str(clean_code) + "&type=germplasm")
        html = page.read().decode("utf-8")
    

        file_name = "TAIR_downloads\Germplasm_" + str(clean_code) + ".txt"
        file = open(file_name, "w")
        file.write(html)
        file.close()

        print("Job " + str(count) + " of " + str(file_length) + " finished.")
        count += 1
        time.sleep(2.5)
    except:
        clean_code = code.rstrip()
        errors.append(clean_code)
        time.sleep(3)

file2 = open("germplasm_errors.txt", "a")
for error in errors:
    file2.write(error + "\n")
file2.close()