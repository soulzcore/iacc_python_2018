# The File object

> In Python, like everything else Files are also considered objects.

> Just like objects in general, files have attributes and methods provided by the Python Standard Library

> Python provides a function called open() which takes a file name as input and creates a file object


**Usage**

```python
#f is the file object created by the open function

f = open('fileName')

```

**Sample File Object Attributes**

> ```name``` : Returns the name of the file

> ```mode``` : File open mode

> ```closed``` : Returns true is file is closed


**Sample File Object Methods**

> ```read(size)``` : Read the file, size is the number in bytes that can be read

> ```close``` : Close the file

> ```write(string)``` : Write the string to the file


**Example**

```python
#Create a new file in PyCharm(New File not Python File ) and name it testFile.txt

#Create a file object f
f = open('testFile.txt')

#Print the attribute name of f
print(f.name)

```


**Full Usage**

```python

#f is the file object created by the open function

f = open('fileName','Mode',Buffering)


```


> fileName : This is the File Name to be opened. Also accepts the full system path of the file ( ex : C:/Users/file.txt)

> Mode : Optional. This tells python the type of operations that will be done on the file. Example : r for reading a file, w for writing to a file. Defaults to r

> Bufferng : Optional, The file is buffered to the given value. If it is 1, every line is buffered, negative value uses system default and anything else is size buffered in bytes.



**Common Modes ( lowercase )**

> r : Read Only
> w : Writing a file only
> rb : read only in binary format
> r+ : read and write
> r+ : write and read. Overwrites if file exists, creates if it doesn’t.
> a : Append ( add to the end of file )
> rb+ : read and write in binary format
> wb : write in binary format



**Example**

```python
#Create a new file in PyCharm(New File not Python File ) and name it testFile.txt

#Create a file object f
f = open('testFile.txt','r+',1)

#Print the attribute name of f
print(f.name)

#Print the attribute mode
print(f.mode)

```
