# Methods

> Methods are functions defined in a class

> Methods usually define the behavior of the class

> Methods just like functions can take multiple arguments

> Methods should always define an argument called ‘self’

> Self in python classes refer to the instance or the object created from the class

> For Example, in the example from the previous slide dog1 and dog2 are 2 objects, self in dog1 refers to dog1 and self in dog2 refers to dog2

> When calling a method, the argument self need not be passed

**Usage**
```python
def methodName(self,arg1,arg2..):
     #Method logic
     statemet1;
     statement2;
     #Call the method methodName
     methodName(arg1,arg2)
```

**Example**
```python
#Create class dog, this can be used to create multiple dog objects
class dog:
    'This class represents a dog'
    #Class variable or attribute name to hold the dogs breed
    breed = 'Rocky'

    #Creating a method to make the dog Bark( behavior )
    def bark(self):
        print('Bow Wow!!')

#Create an instance of the dog and call it dog1, dog1 is a new object created from the dog class
dog1 = dog()

#Get the description of the class dog and print it
dog1_class_description = dog1.__doc__
print(dog1_class_description)

#Get the attribute breed of dog1 and print it
dog1_breed = dog1.breed
print('Dog1\'s breed is : ' + dog1_breed)

#Make the dog bark
dog1.bark();

```
