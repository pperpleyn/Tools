import os

global_list: list = []
global_path: str = ""

def isValidPath(path: str) -> bool:
    return os.path.exists(path)

def createDict(path: str) -> list:
    global global_list, global_path
    global_path = path
    files = os.listdir(path)
    items = []
    for file in files:
        print(path + file)
        if os.path.isdir(path + '/' + file):
            items.append({"name": file, "type": "Folder", "path": path + '/' + file})
            continue
        else:
            print("Not a Folder!")
        if os.path.isfile(path + '/' + file):
            items.append({"name": file, "type": "File", "path": path + '/' + file})
            continue
        else:
            print("Not a File!")
        items.append({"name": file})
    global_list = items.copy()
    return items

def sortItemByExtension(path: str = global_path):
    global global_list
    for item in global_list:
        try:
            if item["type"] == "File":
                print (item)
                ext = item["name"].split('.')
                print(ext[-1])

                if not os.path.exists(global_path + '/' + ext[-1]):
                    print(f"Creating {global_path + '/' + ext[-1]} folder...")
                    os.makedirs(global_path + '/' + ext[-1])

        except KeyError:
            print("Invalid Type")
            continue
    # Return path to refresh the list (Future Feature)
    return global_path
