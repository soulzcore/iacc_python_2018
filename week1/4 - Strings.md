

# Strings


> Strings are always enclosed within quotes
>
> Strings without quotes are considered variables
>
> Strings can be concatenated using + symbol



## Sample String Methods


> **capitalize** – capitalizes the first letter of the string
>
> **isalnum** - Returns true if string has at least 1 character and all
> characters are alphanumeric.
>
> **isalpha** - Returns true if string has at least 1 character and all
> characters are alphabetic
>
> **isdigit** - Returns true if string contains only digits
>

**Example**

```python
city = "plano"
cityCapitalize = city.capitalize()
print(cityCapitalize)
```

## Built in Functions


> **len** – returns the length of the string

**Example**

```python
city = "plano"
cityLength = len(city)
print(cityLength)
```

## Exercise


1. *Create and print a string to hold a phone number with only numbers*

```
phone_number = '1276512341';
print(phone_number);
```

2.	*Verify if the phone number has only numbers*

```
is_a_number = phone_number.isdigit();
print(is_a_number);
```

3. *Find the number of digits in the phone number*

```
no_of_digits = len(phone_number);
print(no_of_digits);
```


