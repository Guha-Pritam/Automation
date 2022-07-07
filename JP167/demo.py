file_name = ""
for i in range(5):
    file_name = "file_" + str(i) + "_0" + "AS.txt"
    file = open(file_name, 'x')

print("created ", i + 1, " files")
