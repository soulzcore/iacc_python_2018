# Modules

> Modules are python files which can be reused ( think how functions
> are reused )

> Modules can be imported into other python files and the functions/
> variables defined in the modules can be reused in the code

> Python provides many built in modules


**Usage**
```python
#testModule.py file
#Defining function named functionname
def functionname(arg1,arg2,arg3):
	"statement1"
	"statement2"
	return "value";
```

```python
#New python file
#newFile.py
import testModule;

testModule.functionname(‘value1’,value2,[1,2,3])

```

**Example - Using a Custom Module**

```python
#testModule.py file
def convertInchesToCentimeter(height_in_inches):
	height_in_centimeters = int(height_in_inches) * 2.54;
	return height_in_centimeters;
```
```python
#newFile.py
import testModule

height = raw_input(‘Enter height in inches >>>’);
height_in_centimeters = testModule.convertInchesToCentimeter(height);
print(‘Height in centimeters  : ’, height_in_centimeters);

```

**Example - Using a in built Module**
```python
#import the time module
import time as dt

#print current time
print dt.strftime("%c")
#Tell the program to sleep for 10 seconds
dt.sleep(10)
#Execution from here will be resumed after 10 seconds
print dt.strftime("%c")
```


**PyPi**

> PyPi or Python Package Index is an publicly available online
> repository of packages or modules

> Most of the modules are free to use

> Users can create and upload their own modules

> PIP is a command line tool to install modules from PyPi

> Modules can be installed manually without PyPi

**Example – Install USZipCode module using pip**

>Link : https://pypi.python.org/pypi/uszipcode#install

>Open command prompt and type :

```shell
pip install uszipcode
```
>After installation is successful create a new python file and write the following code :

```python
#import ZipcodeSearchEngine function from uszipcode module
from uszipcode import ZipcodeSearchEngine

search = ZipcodeSearchEngine()
zipcode = search.by_zipcode("75070")
print(zipcode)
```

# Hands on Exercises

1) Install the Wikipedia module from PyPi and recreate the examples on the PyPi page
