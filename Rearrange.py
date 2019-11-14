import os
import glob

path = os.path.dirname(os.path.realpath(__file__))

A = None
B = None
fileType = None

f= open("FileAtoB.txt","r")
if  f.mode == 'r':
    contents = f.readlines()
    A = contents[0]
    B = contents[1]
    fileType = contents[2]
f.close()



txtfilesA = []
pathA = path + '\\' + A.strip() + '\\*' + fileType
print("Getting files in  location A")
for file in glob.glob(pathA):
    txtfilesA.append(os.path.basename(file))

pathB = path + '\\' + B.strip() + '\\**\\*' + fileType
txtfilesB = []
print("Getting files in  location B")
for file in glob.glob(pathB,recursive=True):
    txtfilesB.append(os.path.basename(file))

result = set(txtfilesA) - set(txtfilesB)
print("attempting to Link files from A -> B")
totalFiles = len(result)
for fileA in result:
    src = path + '/' + A.strip() + '/' + fileA
    dst = path + '/' + B.strip() + '/' + fileA
    os.link(src,dst)
print("Copied " + str(totalFiles) + " files from A -> B")
  


txtfilesB2 = []
for file in glob.glob(pathB,recursive=True):
    txtfilesB2.append(file)

result = set(txtfilesB) - set(txtfilesA)
print("attempting to Link files from B -> A")
totalFiles = len(result)
for fileB in result:
    dst = path + '/' + A.strip() + '/' + fileB
    srcPath = None
    for fileB2 in txtfilesB2:
        srcPath = fileB2 if os.path.basename(fileB2) == fileB else srcPath
    os.link(srcPath,dst)

print("Copied " + str(totalFiles) + " files from B -> A")




'''
txtfilesA = []
for file in glob.glob(path + '/A/*.txt'):
    txtfilesA.append(file)

txtfilesB = []
for file in glob.glob(path + "/B/**/*.txt",recursive=True):
    txtfilesB.append(file)

result = set(os.path.basename(txtfilesA)) - set(os.path.basename(txtfilesB))
for fileA in result:
    print("no files in B, linking all!")
    src = path + '/A/' + fileA
    dst = path + '/B/' + fileA
    os.link(src,dst)

result = set(os.path.basename(txtfilesB)) - set(os.path.basename(txtfilesA))
for fileB in result:
    dst = path + "\\A\\" + fileB
    srcPath = None
    for fileB2 in txtfilesB:
        srcPath = fileB2 if os.path.basename(fileB2) == fileB else srcPath
    os.link(srcPath,dst)
'''




    


            
