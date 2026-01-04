newFile = open("newfile.txt", "w")
newFile.write("Hello, World!")
newFile.close()

# This code creates a new file named "newfile.txt" in write mode,

# writes the string "Hello, World!" to it, and then closes the file.

# If "newfile.txt" already exists, it will be overwritten.

# To verify the content, you can reopen the file in read mode and print its contents:
with open("newfile.txt", "r") as file:
    content = file.read()
    hello = content.strip("Hello, ")
    print(hello)
    print(content)

# Append mode example
with open("newfile.txt", "a") as file:
    file.write("\nMy name is Katlego mashego." \
    "\nI am learning Python file handling." \
    "\nI hope to become proficient in it soon." \
    "\nThank you!")
    file.close()

file = open("newfile.txt", "r")
data = file.read()
print(data)