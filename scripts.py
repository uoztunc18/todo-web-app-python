FILENAME = "items.txt"

def getItems(filepath=FILENAME):
    with open(filepath, "r") as file:
        fileContent = file.readlines()
    return fileContent

def writeItems(item, filepath=FILENAME):
    with open(filepath, "w") as file:
        file.writelines(item)