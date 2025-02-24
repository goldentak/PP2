import os
os.makedirs('txts', exist_ok=True)
for i in range(65, 91):
    s = chr(i)
    file_path = f"LAB6/txts/{s}.txt"

    try:
        with open(file_path, 'x') as f:
            print(f"file {file_path} created!")
    except FileExistsError:
        print(f"File {file_path} already exists!")
    