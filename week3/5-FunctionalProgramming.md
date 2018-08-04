# Functional Programming

> Object Oriented Programming exclusively uses classes to build programs

> Functional programming is an another way to write code.

> Python supports Functional programming in addition to Object Oriented

> In Functional Programming, the code logic is written around Functions

> The basic characteristic of a function in functional programming is that it does not change data that exists outside of the function. ( i,e Functions are not dependent or coupled with any data outside the functions )

> Functions in functional programming are stateless

**Non-Functional approach**

```python
#Variable a defined outside the function
a = 5

#Function to add two numbers, one of the numbers a is defined outside the function
def sum(b):
  return a+b

#Call the sum function
sum(4)
```

**Functional approach**

```python

def sum(a,b):
  return a+b

#Call the sum function
sum(5,4)
```



# Lambdas

> lambda expressions can be used to write functions instead of the def keyword

> Lambda expression starts with the keyword lambda and immediately declares the input arguments then a colon followed by the return statement without explicitly writing return

> The return statement can only be one expression

> Lambda functions can be assigned and used as a variable

> They are also referred to as anonymous functions

> Lambda functions can be passed as arguments to other functions

**usage**

```Python

lambda inputs : return statement

```

**Example of a regular function using def**

```python

#Define a function sum to add two numbers a and b
def sum(a,b):
  return a+b

#Call the function Summer
c = sum(4,5)
print(c)


```



**The same example using Lambda expression**

```Python

sum = lambda a,b : a+b

c = sum(4,5)
print(c)

```
