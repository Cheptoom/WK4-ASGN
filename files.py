#reads a file
with open ("input.txt", "r") as file:
    content=file.read()
    print(content)

# Modify the content
modified_content = content.upper()
#Write the modified content to a new file
with open ("output.txt", "w") as file:
    file.write(modified_content)
    print(modified_content)
#ask the user for a file name and handle errors if the file does not exist or can't be read 
def read_file():
    filename=input("Enter the file name: ")
    try:
        with open (filename, "r") as file:
            content=file.read()
            print(content)          
    except FileNotFoundError:
        print("Error: The file '{filename}' was not found.")
    except PermissionError:
        print("Error: You don't have permission to read the file '{filename}'.")
    except IOError:
        print("Error: Could not read the file '{filename}' due to an I/O error.")
read_file()
