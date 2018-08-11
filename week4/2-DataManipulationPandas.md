# Data Manipulation & Analysis

# Pandas

> Pandas is a python library or package commonly used for data analysis and manipulation

> It is extremely powerful an flexible

> It is being widely adopted in the Data Engineering and Data Science community

> Pandas add support different types of data, some common types are:
> * Tabular data
> * Time series data
> * Matrices

> Pandas support reading and writing to text, csv, excel, sql databases etc…

> Pandas is extremely fast and optimized for performance

> Pandas is built on top of NumPy – Scientific computing package for Python

> Pandas introduce three new data structures
> * Series – One dimensional arrays ( think lists )
> * Data Frames – 2 dimensional data structure  ( Think tables or excel spreadsheets with rows and columns ).
> * Panels – 3 dimensional data structure

**Installation**

> Install pandas from pypi by running the following command in command prompt or console :

```python
pip install pandas

```

# Series

> Series are one dimensional arrays ( ndarrays )

> Ndarrays are multi dimensional data structures defined by numpy – the framework pandas are built on

> Series can be created from lists, dicts , by passing values etc..

> Series consist of an Index and the data

> Index can be pre defined, added later, changed or defaulted to a sequence of numbers

![alt text](https://github.com/soulzcore/iacc_python_2018/raw/master/week4/images/series.png "Pandas Series")


**Series Example**

```Python

#import the pandas module
import pandas as pd

#Create a list of numbers
listOfNumbers = [1,3,5,7,9,0]


#Create a series from the list by applying an index ( by using the series class from the module )
df = pd.Series(listOfNumbers, index=['a','e','i','o','u','z'])

#print the series
print(df)


```


**Example**

```Python
#import the pandas module
import pandas as pd

#Create a list of numbers
listOfNumbers = [1,3,5,7,9,0]


#Create a series from the list by applying an index ( by using the series class from the module )
df = pd.Series(listOfNumbers, index=['a','e','i','o','u','z'])

#print the series
print(df)


#Call the sort_values methid to sort the series
print(df.sort_values())

#Print the value with the row index i
print(df['i'])

#Print the value with the row index u
print(df['u'])


```


**Sample Attributes**

> shape – Returns a tuple of number of rows and columns

> size – Returns the number of items in the Series

> values – Returns the series as an ndarray ( list like )



**Sample Methods**

> describe() – Generates descriptive statistics like count, mean, percentiles etc.

> head(n) – Return first n rows

> tail(n) – Return last n rows

> groupby() – groups values by key

> max() – return max value

> min() – return the minimum value



# Data Frames


> Data Frames are 2 dimensional ndarrays

> Think of it as a table, spreadsheet or a matrix

> Dataframes can be created from multiple series, arrays, dicts, lists, csv files, database tables etc

> Dataframes consist of the data, index and multiple columns

> Index can be pre defined, added later, changed or defaulted to a sequence of numbers



![alt text](https://github.com/soulzcore/iacc_python_2018/raw/master/week4/images/dataframes.png "Dataframes")


![alt text](https://github.com/soulzcore/iacc_python_2018/raw/master/week4/images/dataframes1.png "Dataframes")






**Example**

```python
import pandas as pd

#Create a dict of lists, numbers and words are keys
d = {
    'numbers' : [4, 2, 1, 19],
     'words' : ['a', 'f', 'c', 'z']
     }

#Create a dataframe from d
df = pd.DataFrame(d)

#Print the dataframe
print(df)

```


**Example**
```Python

import pandas as pd

#Create a dict of lists, numbers and words are keys
d = {
    'numbers' : [4, 2, 1, 19],
     'words' : ['a', 'f', 'c', 'z']
     }

#Create a dataframe from d
df = pd.DataFrame(d)

#Print the dataframe
print(df)

#Sort the dataframe by the words column
print(df.sort_values(by='words'))

#Sort by the numbers column in descending order
print(df.sort_values(by='numbers',ascending=False))

#Print the number or rows and columns
print(df.shape)

#Print descriptive statistics
print(df.describe())

```


**Sample Attributes**

> shape – Returns a tuple of number of rows and columns
> size – Returns the number of items in the Series
> values – Returns the series as an ndarray ( list like )


**Sample Methods**

> describe() – Generates descriptive statistics like count, mean, percentiles etc.

> head(n) – Return first n rows

> tail(n) – Return last n rows

> groupby() – groups values by key

> max() – return max value

> min() – return the minimum value
