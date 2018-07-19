
# Flow Control - Loops



## While Loop


> Repeats a group of statements while a given condition is TRUE.
> It tests the condition before executing the loop body.


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

![
](link)


## For Loop

> Repeats or iterate over the items of any sequence, such as a list or a
> string.


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

![
](loop2)
