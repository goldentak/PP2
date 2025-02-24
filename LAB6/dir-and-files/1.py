import os

def list_content(path):
    all_items = os.listdir(path)

    directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
    files = [item for item in all_items if os.path.isfile(os.path.join(path, item))]

    print("all items:: ", all_items)
    print("directories:: ", directories)
    print("files :: ", files)



path = "."
list_content(path)
