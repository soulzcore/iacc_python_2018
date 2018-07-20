


# Data Structures - Lists

> List is a collection of 0 or more items or objects.

> Square bracket is used to represent a list

> Item position numbers are called index

> Index starts from 0

**Usage**

> ```[ ]``` – Empty List
>
> ```["Plano"]``` – A list of 1 string
>
> ```["Plano","Frisco"]``` – a list of 2 strings
>
> ```["Plano","Frisco", 75070]``` – a list of 2 strings and a number
>
> ```["Plano", "Frisco", 75070, ["Allen","McKinney"]]``` – a list with a nested
> list


![List](https://github.com/soulzcore/iacc_python_2018/raw/master/week1/images/lists.png)

    colors = ["red","blue","green"]


## **Accessing items in the list :**

    colors[0] -> This will represent “red”

    colors[1] -> This will represent “blue”

    colors[:] -> ["red","blue","green"]

    colors[1:2] -> ["blue"]

    colors[:1] -> ["red"]
    
    colors[-1] -> ["green"]



![List Slicing](https://github.com/soulzcore/iacc_python_2018/raw/master/week1/images/listslicing.jpg)


> Items can be inserted, removed or replaced in a list using standard
> methods provided by python

> Python provides built in functions for lists

## Common list methods

> **append** : add to the end of the list
>
> **insert** : add at a specific location of the list
>
> **pop** : remove and return item from the list
>
> **remove** : remove an item from the list
>
> **extend** : add list of elements at the end
>
> **sort** : sort the list
>
> **reverse** : reverse the list
>
> **index** : return the lowest index where a item appears
>
> **count** : Count the number of times an item appears in the list



## Built in Functions


> **len** : Get the number of items in the list
>
> **max** : get the item with the max value
>
> **min** : get the item with the lowest value




# Exercise


1.	*Create a list of major cities cities in the US and name it cityList*

```cityList = ["New York","Chicago","LA"]```

2.	*Print cityList*

```print(cityList)```

3.	Print the first city from the list

```print(cityList[0]) ```

4. *Print last city from the list*

```print(cityList[-1])```

5. *Add Houston and Dallas to the list and print the new list*

```
cityList.append("Houston");
cityList.append("Dallas");
print cityList;
```
6. *Add Boston after LA in the list and print it*

```cityList.insert(3,"Boston")
print cityList;
```

7. *Find the rank of Houston in the list*

```print(cityList.index("Houston"));```

8. *Add Toronto to the end of the list and print it*

```
cityList.append("Toronto")
print cityList;
```

9. *Totonto is not a city in the US, lets remove it and print the list*

```
cityList.remove("Toronto");
print cityList;
```

10.  *Find the number of cities in the list*

```print(len(cityList))```


