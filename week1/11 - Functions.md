

# Functions

> Function is a block or unit of code that can be reused.
> Functions often perform a single action.
> Python comes packaged with a lot of
> functions which are called in built functions.
> Functions created by the user are called user defined functions.
>

> Functions begin with the keyword **def** followed by the function name
> and end with  parentheses ( ) followed by the statements which are
> executed when the function is called.
> The code block is always indented.

**Usage**

```python
#Defining function called custom_function_name
def custom_function_name():
	'Statement 1'
	'Statement 2'
	'Statement 3'
```

**Example**

```python
def add_numbers():
	x = 4;
	y = 5;
	sum = x + y;
	print(sum)
```

> Functions can be executed or called via the functions name after they
> are defined.

**Example**

    add_numbers()

**Arguments**

> Functions can accept multiple input parameters( arguments ) which can be passed as 
> comma separated values within the parenthesis after the function name.
> The arguments can be used as variables within the function’s definition
>The arguments can be of any type

**Usage**
```python
#Defining function named functionname
def functionname(arg1,arg2,arg3):
	"statement1"
	"statement2"

#Calling finctioname
functionname(‘value1’,value2,[1,2,3])

```

**Example**

```python
def add_numbers(x , y):
    sum = x + y;
    return sum

add_numbers(4,5)

```

**Return Values**

> Functions can return values back to the statement from where the
> function is called.
> The values returned can be of any type including `None`
> The keyword `return` is used for returning values

**Usage**

```python
#Defining function named functionname
def functionname(arg1,arg2,arg3):
	"statement1"
	"statement2"
	return "value";

#Calling functioname, the result of the statement below will be same as 'value' which was returned in the function
result = functionname('value1',value2,[1,2,3])

```

# Variable Scope

**Local Variables**

> Variables defined within the function block are called local variables
> and they can be accessed only within the function

**Global Variables**

> Variables defined outside functions are called global variables and
> they can be accessed throughout the python and from within functions.

**Example**
```python
#y is a global variable
y = 5
def add_numbers() :
   #x is a local variable
   x = 4
   sum = x + y;
   print( sum )
add_numbers()
#This will throw an error
print(x)
```
# Built in Function - Input

**Providing input via the console**

> Raw Input is a Python built in function

>It presents a prompt to the user during runtime, gets input from
> the user and presents it to the program as a string.

**Usage**

```python
input(‘What is your name? >> ‘)
```

> When this statement is executed, you would notice the string ‘What is
> your name? >> ‘ appear on the console.

> If you click or press any key, a cursor will show up.
 
> Now, the console is ready to accept your input.

> Enter any string and hit the ENTER key.
 
> This will signal the console to pass on your input to the program or
> more specifically the raw_input statement

> The raw_input statement can be assigned to a variable.

> After the raw_input executes, it will result in the variable being
> assigned the value which was entered via the console

> The variable can be used just like any other variable in python.

```python
name = input(‘What is your name? >>’);
print(name);
```

# Recursive Functions

> Recursive functions are functions which call themselves

> Make sure there is some sort of exit condition to prevent getting
> into an infinite loop

**Eaxmple**

```python
#Define a function
def calculateFactorial(n):

    #Check to see if the number is 1 and return 1, since 1! is always 1
    if n == 1:
        return 1

    #If the number passed to the function is not 1, calculate (n-1)! and multiple it to the number
    else:
        return n * calculateFactorial(n - 1)

#Calculate the factorial of 3
factorial = calculateFactorial(3)
print(factorial)

```

# Exercise

1. Create a function to convert height given in feet to inches ( 1 ft = 12 in )
```python
#Define the function convert_height
def convert_height(height_in_feet):
	height_in_inches = height_in_feet * 12
	return height_in_inches

#Call function
height_in_inches = convert_height(7)

#Print the result
print("Height in inches : ", height_in_inches)
```

2. Write a program to accept multiple lines using input
3. Create a function to accept two strings and print the string created by concatenating the two 
4. Write a program to generate the Fibonacci sequence of 10 numbers
5. Password strength checker : Create a function to accept a string  and verify if it conforms to the following format – between 8 to 12 characters long, atleast 1 upper case character, atleast 1 number and 1 special character which can be one of ’@,#,$,% or &’
