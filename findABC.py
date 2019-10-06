import os

superGlobalCounter = 0

def recursiveTraversal(path):
    if os.path.isfile(path):
        checkFile(path)

    elif os.path.isdir(path):
        paths = os.listdir(path)

        for subPath in paths:
            recursiveTraversal(f"{path}/{subPath}")
    
    else:
        print("Somethin went wrong")

    
def checkFile(path):
    f = open(path, "r")

    if (checkFor(f.readline())):
        global superGlobalCounter 
        superGlobalCounter += 1
        print(f"Match #{superGlobalCounter} in: {path}")


def checkFor(ABC):
    if ABC == "AAA":
        return True

    return False


def main():

    recursiveTraversal("root/")


if __name__ == "__main__":
    main()