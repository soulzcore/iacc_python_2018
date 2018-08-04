
# Other File methods

**Closing Files**

> It’s a good practice to always close a file after you are done working with it

> ```close()``` : The close method of the file object is used to close an open file connection

> After you use the close method on a file object any further attempts to read or write the file will fail

**Example**

```python

#Open testFile2.txt in write mode, overwrite if exists, create if doesnt exist
f = open('testFile1.txt','a')

#String to be written in the new file, \n creates a new line
string1 = 'This will be added to the end of the file'

#Write to the file
print(f.write(string1))

#Closing the file connection
f.close()

#The file read will fail with Value Error
print(f.read())

```


**Seek**

> The seek file method can be used to instruct python to go to a certain position in the file.

> Any subsequent read or write operations will be done starting from the position you specified in the seek method


**Usage**

```python
f.seek(postion, starting_point)

```

> Position : The position to seek to ( in bytes ).

> Starting_point : Optional, This can be 0,1 or 2. 0 to start from the beginning, 1 to use current position and 2 to start from the end. Defaults to 0. The file has to be opened in binary format ( using b ) to be able to seek from the end.



**Example**

```python
#Open a file for reading
f = open('testFile1.txt','r')

#Go to 10th byte from the start of the file
f.seek(10,0)

#This would print the file from position 10 to the end
print(f.read())

#Go to the 30th byte from the start of the Document
f.seek(30,0)


print(f.read())

```




**Tell**

> The tell method is used to determine what position in the file python is currently working at

> Any subsequent read or write operations will be done starting from the position you specified in the seek method


**Usage**
```python
f.tell()

```

**Example**

```python

#Open a file for reading
f = open('testFile1.txt','rb')

#Go to 10th byte from the start of the file
f.seek(10,0)

#Print the current position, which is 10 after the seek
print(f.tell())

#Go to the 10th byte from the end of the document
f.seek(10,2)

#This will return the current position, which is total bytes - 10 after the previous seek
print(f.tell())

```


# Exercises

**Write a program to create a new file named "newFile.txt" and write atleast 5 lines of text.Read the "newFile.txt" and copy the contents of the file into another file named "copyOfnewFile.txt"	***



**Download the file from the following URL to your computer : http://media.pearsoncmg.com/bc/bc_production/media_development/media_manager_ircd_cdroms/MM_readme.txt
Write a program to read the file and count the number of words in the file.**
