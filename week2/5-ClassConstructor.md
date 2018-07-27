# Class Constructor

> Constructor is a method which Python calls whenever an instance of a class is created

> Having a constructor is optional, Python will only call it if it exists

> Constructor method is always named ```__init__```

> Contructor can take input arguments just like regular methods

> Constructor will always have self as a parameter like methods : ```__init__(self)```

**Usage**
```python
#Create a method __init__ within the class
def __init__(self,arg1,arg2..):
  #Constructor logic
  statement1;
  statement2;

  ```


**Example**

```python

#Create class dog, this can be used to create multiple dog objects
class dog:
    'This class represents a dog'
    #Class variable or attribute name to hold the dogs name
    breed = 'Bulldog'

    #Creating a constructor which will be called everytime a new object is created
    def __init__(self):
        print(self.breed)
        print('Dog Object created')

#Create an object dog1 from dog
dog1 = dog()

#Create an object dog2 from dog
dog2 = dog()

```
