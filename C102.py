import os
import shutil
sourcePath="D:/Anu"
destPath="D:/Shreya"
listOfFiles = os.listdir(sourcePath)
print(listOfFiles)
for file_name in listOfFiles:
    name, ext = os.path.splitext(file_name)
    print(name)
    print(ext)
    if ext=='':
        continue
    if ext in ['.rtf' , '.xlsx' , '.txt']:
        path1 = sourcePath+'/'+file_name
        path2 = destPath+'/'+"My Files"
        path3 = destPath+'/'+"My Files"+'/'+file_name
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
        print(path1)
        print(path2)
