
# Flow Control - Loops



## While Loop


> Repeats a group of statements while a given condition is TRUE.
> It tests the condition before executing the loop body.

![
](https://github.com/soulzcore/iacc_python_2018/raw/master/week1/images/loops.png)

## Usage


```python
while expression:
	statements;
else:
	This is executed if expression becomes false
```

## Example

```python
count = 0
while count < 5:
	print(count)
	count = count + 1
```

The above example will print 0 to 4




## For Loop

> Repeats or iterate over the items of any sequence, such as a list or a
> string.

![
](https://github.com/soulzcore/iacc_python_2018/raw/master/week1/images/loops2.png)

## Usage


```python
for item in list:
	statements;
else:
	This is executed if list runs out of items;
```


## Example



```python
numList = [0,1,2,3,4];
for num in numList:
	print num;
```

The above example will print 0 to 4


