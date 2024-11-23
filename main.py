import os

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"file {filename} created")
    except FileExistsError:
        print(f"File {filename} already exists")
    except Exception as E:
        print("An error occured")

def view_all_files():
    files = os.listdir()
    if not files:
        print("No files found")
    else:
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File {filename} deleted.")
    except FileNotFoundError:
        print(f"File {filename} does not exist.")
    except Exception as e:
        print("An error occurred.")

def read_file(filename):
    try: 
        with open("sample.txt", "r") as f:
            content = f.read()
            print(f"File {filename} opened for reading.")
    except FileNotFoundError:
        print(f"File {filename} not found")
    except Exception as e:
        print("An error occured")

def edit_file(filename):
    try:
        with open("sample.txt", "a") as f:
            content = input('Enter you text here: ')
            f.write(content + "/n")
            print(f"Content added to '{filename}' successfully.")
    except FileNotFoundError:
        print("File does not exist.")
    except Exception as e:
        print("An error occurred.")

def main():
    while True:
        print("FILE MANAGEMENT APP")
        print("1. CREATE FILE")
        print("2. VIEW ALL FILES")
        print("3. REMOVE FILE")
        print("4. READ FILE")
        print("5. EDIT FILE")
        print("6. EXIT")
