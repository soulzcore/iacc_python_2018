# Map

> Map is a built-in function which accepts one or more iterable data type ( list, tuple etc..) and a function as input arguments/parameters

> It applies the function passed to every element of the given iterable and returns a new list with the new values

> For Example : There is a list of 5 numbers and a function 'a' which takes a number and multiplies it by 10.
> If you pass them both to a map, the function a is applied to every item in the list resulting in a new list with the new values  

**Usage**

```Python
map(function, iterable)
```

**Example**

```python

#Defining a list A
listA = [1,2,3,4,5]

print(listA)

#Defining the functionA
def functionA(n):
  return n * 10


#Applying the map function
mapA = map(functionA, listA)

#Converting the map object into a list
newListA = list(mapA)

#Printing the new list
print(newListA)

```


**Example Using Lamdba Function**

```python

#Defining a list A
listA = [1,2,3,4,5]

print(listA)

#Using the lambda function in map
mapA = map(lambda x : x*10, listA)

#Converting the map object into a list
newListA = list(mapA)

#Printing the new list
print(newListA)


```


**Example with multiple lists**

```python

#Defining a list A
listA = [1,2,3,4,5]

listB = [1,2,3,4,5]

print('List A : ', listA)

print('List B :', listB)

#Applying the map function
mapA = map(lambda x,y : x*y, listA, listB)

#Converting the map object into a list
newListA = list(mapA)

#Printing the new list
print(newListA)

```



# Filter

> The Filter function accepts a function and an iterable ( just one unlike map)

> The function which is passed to filter has to return a boolean ( True or False)

> Filter applies the function passed to every item in an iterable and returns a new list with only the items which returned true


**Usage**

```Python
filter(function, iterable)
```


**Example**

```Python

#Define a list of numbers
listA = [1,21,12,4,11]

#Define a function which returns true if the number passed is greater than 10
def functionA(n):
    return (n > 10)

#Pass function A and listA to the filter
filterA = filter(functionA, listA)

#Convert filter object into a list
newListA = list(filterA)


#Print the new list, only numbers greater than 10 will appear in the result
print(newListA)

```


**Example using lambda**


```Python

#Define a list of numbers
listA = [1,21,12,4,11]

#Use Lambda function to filter
newListA = list(filter(lambda x:x>10, listA))

#Print the new list, only numbers greater than 10 will appear in the result
print(newListA)

```



# Reduce

> Reduce accepts a function and a iterable as the input arguments

> It reduces or converts the given iterable(list) into a single value

> The passed function should accept 2 arguments and return a single value

> The function which is passed is applied to the first 2 elements in the given list resulting in a single output, the function is again applied to the output from the previous operation and the next item in the list. This process is repeated until there is only 1 item remaining

> The reduce function is available in the functools built in module. ```from functools import reduce``` imports the function into the current file.


![alt text](https://github.com/soulzcore/iacc_python_2018/raw/master/week3/images/filter.png "Filter Function")



**Usage**

```Python

reduce(function, iterable)

```



**Example**

```Python

#Import the reduce function from functools module
from functools import reduce

#Define a list of numbers
listA = [1,2,3,4]

#Define a function to add 2 numbers
def functionA(x,y):
    return x+y

#Pass functionA and listA to reduce
reduceA = reduce(functionA,listA)

#Print the result
print(reduceA)

```



**Example Using Lambda**

```python

#Import the reduce function from functools module
from functools import reduce

#Define a list of numbers
listA = [1,2,3,4]

#Reduce listA using a lambda function
print(reduce(lambda x,y : x+y,listA))



```
