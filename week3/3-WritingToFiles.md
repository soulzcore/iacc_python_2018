**Writing To Files**


> Files have to be opened in a mode which supports writing( ex : w, r+,w+)

> The file object has a few different methods for writing a string to the file

> ```write('string')``` : Writes the entire string to the file

> ```writelines(List)``` : Writes the Strings in a List to a file


**Full Usage**

```python

#f is the file object created by the open function
f = open('fileName','Mode')

#Some string which has to written to fileName
fileContent = 'Some String'

stringList = ['String1', 'String2', 'String3']

# Write fileContent to file
f.write(fileContent)

#Write the strings in the list stringList to fileName
f.writelines(stringList)

```

**Example**

```python

#Open testFile2.txt in write mode, overwrite if exists, create if doesnt exists
f = open('testFile1.txt','w')

#String to be written in the new file
fileContent = 'This is a test file'

#Write fileContent to the file
f.write(fileContent)

```

**Example**

```python

#Open testFile2.txt in write mode, overwrite if exists, create if doesnt exist
f = open('testFile1.txt','w')

#String to be written in the new file, \n creates a new line
string1 = 'This is 1st line\n'
string2 = 'This is a 2nd line\n'
string3 = 'This is 3rd Line\n'

#Create a list of string1, string2, string3
stringList = [string1,string2,string3]

#Write list of strings in stringList to the file
f.writelines(stringList)

```




**Example**

```python
#Open testFile2.txt in write mode, overwrite if exists, create if doesnt exist
f = open('testFile1.txt','a')

#String to be written in the new file, \n creates a new line
string1 = 'This will be added to the end of the file'

#Write to the file
f.write(string1)

```
