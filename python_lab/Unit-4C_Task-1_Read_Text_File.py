try:
    file = open("sample.txt", "r")
    content = file.read()

    print("File Content:")
    print(content)

    file.close()

except FileNotFoundError:
    print("Error: sample.txt not found.")
