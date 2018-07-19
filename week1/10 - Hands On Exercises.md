
# Hands On Exercises


1. *Write a program to determine if a given number say 5 is odd or even*


```python
num = 5;
mod = num % 2;
if mod > 0:
	print(num, 'is an odd number');
else:
	print(num, 'is an even number');
```

2.  *Given a list of numbers( numList) find all the numbers in the list which are less than 10 and put them in a  new list ( newList )*

```python
numList = [1,12,5,7,8,9,12,4,8];
newList = [];
for num in numList:
	if num < 10:
	print num;
	newList.append(num);
print newList;

```

3.  *Write a program to determine if a given word is a palindrome*

```python
word = 'abc'
letters = list(word)
is_palindrome = True
for letter in letters:
	if letter == letters[-1]:
	letters.pop(-1)
else:
	is_palindrome = False
	break
print is_palindrome
```
4. *Write a python program to sum all the items in a list*

5. *Write a python program to merge two lists into a dict*

	*Example :*
	```python
	fruits = [‘oranges‘, ‘apples’,’peaches’]
	quantity = [’12,14,15’]
	result = {‘oranges’:12,’apples’:14,’peaches’:15}```

6. Write a python program to determine if a given number is a prime number
