# Classes

> Classes are blueprints from which objects are created

> Objects are created from classes

> Classes contain the definition or code of objects ( attributes and methods )

> Classes can be instantiated to create an object

> You can create many many instances or objects with different attributes and behaviors from a single class

**Usage**
```python
class className :
    ‘Class description and documentation’
    #variables/attribute/property
    var = ‘sample variable’

```
> An instance of the class can be created or instantiated using the systax : ``` class className() ```

> The instance can be assigned to a variable

> Example : ``` class_var = className() ```

> ``` class_var``` represents an instance of the class or an object

> Class attributes can be accessed using the dot operator

> Example : ``` class_var.__doc__ ``` gets the description of the class

> ``` class_var.var ``` represents the variable ``` var ``` defined in the class with the value of ``` 'sample variable' ```

**Example**
```python
#Create class dog, this can be used to create multiple dog objects
class dog:
    'This class represents a dog'
    #Class variable or attribute name to hold the dogs breed
    breed = 'Bulldog'

#Create an instance of the dog and call it dog1, dog1 is a new object created from the dog class
dog1 = dog()

#Get the description of the class dog and print it
dog1_class_description = dog1.__doc__
print(dog1_class_description)

#Get the attribute breed of dog1 and print it
dog1_breed = dog1.breed
print('Dog1\'s breed is : ' + dog1_breed)

```

**Example**

```Python


#Create class dog, this can be used to create multiple dog objects
class dog:
    'This class represents a dog'
    #Class variable or attribute name to hold the dogs breed
    breed = 'Bulldog'

#Create an instance of the dog and call it dog1, dog1 is a new object created from the dog class
dog1 = dog()

#Get the description of the class dog and print it
dog1_class_description = dog1.__doc__
print(dog1_class_description)

#Get the attribute name of dog1 and print it
dog1_breed = dog1.breed
print('Dog1\'s breed is : ' + dog1_breed)


#Create 2nd dog object called dog2
dog2 = dog()

#Get the description of the class dog and print it
dog2_class_description = dog2.__doc__
print(dog2_class_description)

#Get the attribute breed of dog2 and print it
dog2_breed = dog2.breed
print('Dog2\'s breed is : ' + dog2_breed)

```
