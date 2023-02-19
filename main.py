import os.path
sum=0
if os.path.isfile('content.txt'):
    with open('content.txt') as content:
        files = content.read()
        filesList = files.split()
        for file in filesList:
            fileName = file+'.txt'
            if os.path.isfile(fileName):
                with open(fileName) as currentFile:
                    numberLine = currentFile.read()
                    numberList=numberLine.split()
                    for i in numberList:
                        flag = True
                        try:
                            int(i)
                        except ValueError:
                            flag = False
                        if flag == True:
                            sum=sum+int(i)
            else:
                print("Файл " + fileName + "не існує")
                continue
else:
    print("Файл content не існує")
print(sum)