# Reading Files


> Files have to be opened in a mode which supports reading ( ex : r, r+,w+)

> The file object has a few different methods for reading the content of the file

> ```read()``` : Returns the entire file as a string

> ```read(n)``` : Returns the first n bytes of the file

> ```readline()``` : Returns a single line of the file as a string

> ```readlines()``` : returns all the lines as a list


**Full Usage**

```python

#f is the file object created by the open function
f = open('fileName','Mode')

# Returns the entire file as a string
f.read()

#Returns the first n bytes of the file
f.read(n)

#Returns a single line of the file as a string
f.readline()

# returns all the lines as a list
f.readlines()


```



**Example**

```python

#Open the testFile.txt and type a few lines of text and save it

#Open testFile.txt in read only mode
f = open('testFile.txt','r')

#Print the file Name
print(f.name)

#Read and print the entire file content
print(f.read())

```



**Example**

```python

#Open testFile.txt in read only mode
f = open('testFile.txt','r')

#Read and print the 1st line
print f.readline()

#Read and print the 2nd line
print f.readline()

#Read and print the 3rd line
print f.readline()
```

**Example**

```python
#Open testFile.txt in read only mode
f = open('testFile.txt','r')

#Read and print all lines as list
print(f.readlines())
```


**Example**

```python
#Open testFile.txt in read only mode
f = open('testFile.txt','r')

#Python provides an iterator for file which makes it easy to read lines in a loop
for line in f:
    print(line)

```
