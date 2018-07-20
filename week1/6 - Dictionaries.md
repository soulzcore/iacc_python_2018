

# Dictionaries





> Dictionary is a collection of 0 or more items.

> Each item concists of a unique key and a corresponding value
> separated by a colon
>
> Example : ```'state':'Texas'```

> Set of braces are used to represent a dictionary
>
> ```{ }``` – Empty Dict or Dictionary

> ```{'state':'Texas', 'city':'Plano'}``` – Two items or two key value pairs  
>
>``` {'state':'Texas', 'city':'Plano', 'seasons':['Summer','Spring']}```– a dict of 3 items where the last value is a list



![
](https://github.com/soulzcore/iacc_python_2018/raw/master/week1/images/dict1.png)

    sample = {'a':'alpha','b':'omega','g':'gamma'}  
    
    

**Accessing items in the dict**

> ```Sample['a']``` -> This will return the value ‘alpha’
>
> ```Sample['d'] = "delta"``` -> This will add 'd':'delta to the dict'

**Common dict methods**

> ```clear``` : remove all elements from the dict
>
> ```keys``` :returns a list of keys in the dict
>
> ```values``` : returns a list of values in the dict

**Example**
```python
sample = {'a':'alpha','b':'omega','g':'gamma'}  
values = sample.values()
print(values)

```

**Functions**

> ```len``` : Get the number of items in the dict
>
> ```str``` : get the string representation of the dict

**Example**

```python

dictLength = len(sample)
print(dictLength)

```


## Exercise


1. *Create a dictionary of a restaurant menu with 3 items as keys and their prices as values*

```python
menu = {"Cheese Burger" : 10, "Caesar Salad" : "8", "Fries" : 3.25}
```

2.  *Print the menu*

```python
print(menu)
```

3. *Print the price of a Cheese Burger*

```python
print(menu['Cheese Burger'])
```

4. *Print all items in the menu*

```python
print(menu.keys())
```

5. *Does the restaurant have ‘Lemonade’ in the menu..?*

```python
print('Fries' in menu)
```

6. *How many items are in the menu*

```python
print(len(menu));
```

7. *Add ‘Lemonade’ to the menu and set the price to 2.5*

```python
menu['Lemonade'] = 2.25;
```

8. *Update the price of ‘Cheese Burger’ to 9*

```python
menu['Cheese Burger'] = 9;
```

9. *Print the new menu*

```python
print(menu);
```
