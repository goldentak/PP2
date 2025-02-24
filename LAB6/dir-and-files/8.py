import os

def delete_file(file_path):
    if not os.path.exists(file_path):
        print(f"{file_path} does not exist.")
        return
    
    if not os.access(file_path, os.W_OK):
        print(f"Cannot access {file_path}.")
        return

    try:
        os.remove(file_path)
        print(f"{file_path} deleted.")
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")

file_path = "LAB6/dir-and-files/file.txt"
delete_file(file_path)
