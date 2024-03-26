file_origin = open("D:\OneDrive - UMH\Manuscritos\Revisión\Germoplasmas\germplasm.txt", "r")

codes = file_origin.readlines()
codes_refined = list(dict.fromkeys(codes))

file_destiny = open("D:\OneDrive - UMH\Manuscritos\Revisión\Germoplasmas\germplasm_refined.txt", "w")

for code in codes_refined:
    file_destiny.write(code)

file_origin.close()
file_destiny.close()