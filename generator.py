
import os
import random

def makefolder(path):
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)



def createDirs():
    startPath = f"{os.getcwd()}/root"
    makefolder(startPath)

    for i in range (1, 10):
        path1 = f"{startPath}/firstlevel{i}/"
        makefolder(path1)

        for j in range(1, 10):
            path2 = f"{path1}/secondlevel{j}"
            makefolder(path2)
                        
            for k in range(1, 10):
                path3 = f"{path2}/thirdlevel{k}"
                makefolder(path3)

                for l in range (1, 10):
                    path4 = f"{path3}/fourthlevel{l}"
                    makefolder(path4)

                    for m in range (1, 10):
                        path5 = f"{path4}/fifthlevel{m}"
                        makefolder(path5)
                        
                        for n in range(1, 5):
                            path6 = f"{path5}/file{n}.txt"
                            f = open(path6, "w+")
                            for o in range(3):
                                f.write(str(chr(random.randint(65,90))))
                            f.close()
                            





def main():
    print("Hello World")
    createDirs()













if __name__ == "__main__":
    main()