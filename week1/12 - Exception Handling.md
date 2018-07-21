# Exceptions

> Exceptions are errors generated while the python program is
> executing.

> Exceptions usually throw an error

> Exceptions stop the program from further execution



**Example**

```python
print('2' + 2);
```
Running the code above return the following error :


    TypeError: cannot concatenate 'str' and 'int' objects

> There are different types of exceptions.

> In the example provided it is ‘TypeError’

> Exceptions can be built in or user defined exceptions

**Some Built in Exceptions**

> **ImportError**
>
> **IndexError**
>
> **KeyError**
>
> **NameError**
>
> **TypeError**
>
> **ZeroDivisionError**


# Exception Handling

> The technique used to deal with exceptions that can potentially
> terminate the execution of the program is called Exception Handling

> Exception Handling is used to guard against exceptions and also to
> provide an alternative way for the code to continue execution

> If you suspect that a piece of code has a possibility of throwing an
> exception and would like to take an action if an exception is thrown,
> enclose the code within a try block and the subsequent action to take
> will go in an except block ( think if – else statements )

**Basic Usage**

```python
#Enclose code which might raise an exception in a try block

try:
	"some statements here";
	"more statements here";

#Except block will be executed when any statement within the try block raises an exception

except:
	"do something";
	"something else";

```


**Full Usage**

```python
#Enclose code which might raise an exception in a try block

try:
	"some statements here";
	"more statements here";

#Except block to handle certain type of exceptions, in this case TypeError

Except TypeError:
	"do something if it’s a TypeError";

#Except block to handle IndexError

Except IndexError:
	"do something if it’s a IndexError";

#Except block to handle exceptions which are neither TypeError or IndexError

Except:
	"do something if its neither a TypeError or IndexError";

#The Else block will be executed if no exceptions are raised and the try block executes successfully

Else:
	"do this if there were no exceptions raised";

#The finally block executes in all cases – with or without exceptions

Finally:
	"do this no matter what happens";

```


***Example***

```python
var = input('Enter a random number >>> ');


def div(var):
    print(10 * (1 / int(var)));


def prnt(var_name):
    print(4 + var_name * 3);


def add(var):
    print(var + 2);


try:
    div(var)
    prnt(var)
    add(var)

except ZeroDivisionError:
    print("Error : Somebody tried to divide by 0")

except NameError:
    print("Error : Variable does not exist")

except TypeError:
    print("Error : Somebody is trying to add a number and a string!")

except:
    print("Error : Something got messed up and I am not sure what!")

else:
    print("All statements were successful")

finally:
    print("I will always be here!")

```


# Raising Exceptions

> The exceptions we have worked in the last few slides were generated
> by Python
>
> The developer can programmatically raise exceptions as well
>
> Exceptions raised by the developer can be the standard exceptions
> provided by python or can be user defined exceptions
>
> Example : The developer would like to raise an exception if a certain
> condition is not met.

**Usage**
```python
If x > 10 :  
	raise Exception
```

**Example**
```python
try:
	#Throw a Name Error exception
	raise NameError("I am raising a Name Error")

#Catch the Name Error exception
except NameError:
	print("There was a name error")

```


# Assertions

> Assertions are checks you can put in place to test some conditions

> These are very similar to if conditions

> Assertions can be used for testing and debugging purposes

> Assertions can be used to check validity of input and output of a
> function

> An Exception is thrown if the assert statement is not satisfied

**Usage**

```python
assert SomeCondition, "fail message"
```

**Example**

```python
#This is an assertion
assert 2 + 2 == 5, 'No, 2 plus 2 is not equal to 5'


```

