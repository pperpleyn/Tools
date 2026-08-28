import os, platform

global_list: list = []
global_path: str = ""

def isValidPath(path: str) -> bool:
    """
    - Verify if a given path is a valid one.
    """
    return os.path.exists(path)

def sanitizePath(pathStr: str) -> str:
    """
    - Ensures the path follows a proper structure to avoid typo and mistakes on directory creation or access.
    """

    global global_path
    os_name = platform.system()
    print("Currently running at", str(os_name))
    print(f"Base Path: {pathStr}")

    x = pathStr.split('/')
    # Splits the given string by the slashes which is common across OS
    print("Current Dir:",x)
    # match os_name:
    #     case "Linux":
    #         x.insert(0, '/')
    #     case "Darwin":
    #         exit()
    # # For OS Compatibility, for now, its only for Linux, I guess?

    newPath = '/' + '/'.join(dir for dir in x if dir != '') + '/'
    # Rebuilds the path for usage. Still needs some tweaking.
    # Noticed the first '/', it should be changed into something dynamic for cross-platform compatibility.

    # print(newPath)
    if not isValidPath(newPath):
        # Verify if the newly rebuild path is valid.
        return False
    

    global_path = newPath
    # Store it to global variable for future usage, reusability.
    return newPath

def createDict(path: str) -> list:
    """
    - Create a list of dictionary, the structure goes like this:
        mainList = [ 
            { 
            'name': fileName, 
            'type': fileType ('Folder' | 'File'), 
            'path': path_to_file + fileName 
            } ]
    """
    global global_list
    path = sanitizePath(path)
    files = os.listdir(path)
    items = []
    x = 0
    for file in files:
        x += 1
        print(f"{x}. {path}{file}", end=" is ")

        if os.path.isdir(path + file):
            items.append({"name": file, "type": "Folder", "path": path + file})
            continue
        else:
            print("not a Folder!", end="\n")
        if os.path.isfile(path + file):
            items.append({"name": file, "type": "File", "path": path + file})
            continue
        else:
            print("not a File!", end="\n")
        items.append({"name": file})

    global_list = items.copy()
    return items

def createDir():
    for item in global_list:
            try:
                if item["type"] == "File":
                    print (item)
                    ext = item["name"].split('.')
                    print(ext[-1])
    
                    if not os.path.exists(global_path + ext[-1]):
                        print(f"Creating {global_path + ext[-1]} folder...")
                        os.makedirs(global_path + ext[-1])
    
            except KeyError:
                print("Invalid Type")
                continue

def sortItemByExtension(path: str = global_path):
    global global_list
    for item in global_list:
        try:
            if item["type"] == "File":
                print (item)
                ext = item["name"].split('.')
                print(ext[-1])

                if not os.path.exists(global_path + ext[-1]):
                    print(f"Creating {global_path + ext[-1]} folder...")
                    os.makedirs(global_path + ext[-1])

                os.replace(global_path + item["name"], global_path + ext[-1] + '/' + item["name"])

        except KeyError:
            print("Invalid Type")
            continue
        
    # Return path to refresh the list (Future Feature)
    print(global_path)
    return global_path
