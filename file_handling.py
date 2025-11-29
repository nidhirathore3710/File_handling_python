import os
print(" Python File Handling Demonstration")
# 1. Writing to a File
with open("example.txt", "w") as file:
    file.write("Hello, this is the first line!\n")
    file.write("Python file handling is powerful.\n")
print("1File created and written successfully.")

# 2. Reading Entire File
with open("example.txt", "r") as file:
    content = file.read()
print("\nReading entire file content:")
print(content)

# 3. Appending to a File
with open("example.txt", "a") as file:
    file.write("This line was appended later.\n")
print("Line appended successfully.")

# 4. Reading File Line by Line
print("\nReading file line-by-line:")
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# 5. Reading into a List
with open("example.txt", "r") as file:
    lines = file.readlines()
print("\nFile content as list of lines:")
print(lines)

# 6. Working with Binary Files
# Create a binary file (example)
binary_data = b"This is binary content"
with open("sample.bin", "wb") as file:
    file.write(binary_data)
print("\n Binary file written successfully.")

# Read binary file
with open("sample.bin", "rb") as file:
    data = file.read()
print("Binary file content:", data)

# 7. Checking if a File Exists
if os.path.exists("example.txt"):
    print("\n File 'example.txt' exists.")
else:
    print("\n File not found.")
os.remove("sample.bin")
print("sample.bin deleted successfully.")
