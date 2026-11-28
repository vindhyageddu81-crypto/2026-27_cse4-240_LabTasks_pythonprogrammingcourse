file = open("sample.txt", "r")
content = file.read()
file.close()

content = content.replace("Python", "Java")

file = open("sample.txt", "w")
file.write(content)
file.close()

print("Word replaced successfully.")