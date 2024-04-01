# File Creation
def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line with text and numbers: 987\n")
    except IOError as e:
        print("Error occurred while creating the file:", e)
    else:
        print("File 'my_file.txt' created successfully!")


# File Reading and Display
def read_file():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of 'my_file.txt':")
            print(file.read())
    except FileNotFoundError:
        print("File 'my_file.txt' not found.")
    except PermissionError:
        print("Permission denied to read the file.")


# File Appending
def append_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1\n")
            file.write("Appending line 2\n")
            file.write("Appending line 3\n")
    except IOError as e:
        print("Error occurred while appending to the file:", e)
    else:
        print("Content appended to 'my_file.txt' successfully!")


if __name__ == "__main__":
    create_file()
    read_file()
    append_file()


