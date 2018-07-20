

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

> Functions can accept input parameters and can return an output value.
> Functions can accept multiple input parameters which can passed as a
> comma separated values within the parenthesis after the function name.
> A value can be returned using the return keyword.

**Example**

```python
def add_numbers(x , y):
    sum = x + y;
	return sum

add_numbers(4,5)

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


**Exercise**

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

	
