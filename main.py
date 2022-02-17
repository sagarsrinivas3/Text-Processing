from pathlib import Path

def createFile(filename, content):
  file = open(filename, 'w')
  file.write(content)
  file.close()
  
def createFileWith(filename, content):
  with open(filename, 'w') as file:
    file.write(content)

def readfilewith(filename):
  with open(filename, 'r') as file:
    content = file.read()
  return content

def removeLastChar(filename, newfile):
  content = readfilewith(filename)
  newContent = content[:-1]
  createFileWith(newfile, newContent)

def removeLastCharMultipleFiles(dir, newfileTerm):
  rootdir = Path(dir)
  for filepath in rootdir.glob("*.csv"):
    if filepath.is_file():
      content = readfilewith(filepath)
      newContent = content[:-1]
      newfileName = newfileTerm+filepath.name
      newfilePath = filepath.with_name(newfileName)
      createFileWith(newfilePath, newContent)

def replaceAWord(dir, replace, sub):
  rootdir = Path(dir)
  for filepath in rootdir.glob("new-*.csv"):
    if filepath.is_file():
      content = readfilewith(filepath)
      newContent = content.replace(replace, sub)
      createFileWith(filepath, newContent)

def MergeFiles(file1, file2, newFile):
  f1Content = readfilewith(file1)
  f2Content = readfilewith(file2)
  newContent = f1Content+"\n"+f2Content
  createFileWith(newFile, newContent)


def replaceLine(file, line):
  with open(file, 'r') as f:
    content = f.readlines()
  content[0] = line
  print(content)
  createFile(file, "".join(content)) 

#create a file
#createFile("sample.txt", "Apple\nBall")

#create a file with "with" operand
#createFileWith(filename="sample.txt", content="Apple\nBall\nDog")

#read a file
#readfilewith(filename="sample.txt")

#remove a last char from line in a file
#removeLastChar(newfile="product.csv", newfile="new-products.csv")

#remove a last char from line from multiple files in a dir
#removeLastCharMultipleFiles(dir="files/", newfileTerm="new-")

#replaace a word in multiple files
#replaceAWord("files/", "price", "Units")

#merge two files
#MergeFiles(file1="new-products.csv", file2="sample.txt", newFile="mergedfile.txt")

# replace a line from text and csv file
#replaceLine(file="new-products.csv", line="ID,NAME,PRICE\n")