

# Conditional Statements



```    
    if expression:
	    "Execute this if expression  is true"
    else:
	    "Execute this if expression is false"
```

 ```  

    if expression a  :
	    "Execute this if expression a  is true"
    elif expression b :
		   "Execute this if expression b is true"
    elif expression c :
		   "Execute this if expression c is true"
    else :
		    "Execute this if none of the above a, b or c are true"
```

![
](https://github.com/soulzcore/iacc_python_2018/raw/master/week1/images/ifelse.png)



## Logical Operators


> ```x or y```  if x is false, then y, else x
>
> ```x and y```  if x is false, then x, else y
>
> ```not x```  if x is false, then True, else False



## Examples



```python
if 10 > 9:
	print('10 is greater than 9')
else:
	print('10 is less than 9')
```

```python

x = 5;
y=10
if x > y:
	print(x, ' is greater than ', y;)
elif x<y:
	print(x, ' is less than ', y);
else:
	print(x, ' is equal to ', y);
```
