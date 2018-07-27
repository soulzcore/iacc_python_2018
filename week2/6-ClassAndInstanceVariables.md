# Class Variables

> Class variables are attributes or variables which will be shared by all instances of the class

> If the class variable is updated from one instance or one single object of a class, it gets updated for all existing instances of the same class

> Class variables are used when an attribute has to be shared across all instances of the class

> Class variables are always defined in the class block of the code

> In our previous examples the  attribute ```'breed.variable'``` is a class variable since it is shared by ```dog1``` and ```dog2```

> Class variables can be accesed using the ``` className.variableName``` instead of instance Name ( Example ```dog.breed``` )

> Class variables can be updated using ```className.variableName = 'New Value'```



**Example**

```python
class dog :
   #Class variable
   breed = 'Poodle'

#Accesed via the class Name
print(dog.breed)

#Create new instance dog1
dog1 = dog()

#Access variable breed via dog1 instance name
print(dog1.breed)

#Create new instance dog2
dog2 = dog()

#Access variable breed via dog2 instance name
print(dog2.breed)

```



# Instance Variables:

> Instance variables are attributes which are unique to each instance

> Changing an instance variable in one instance does not change it for any other instances

> Instance variables are not defined within the class block

>Instance variables are referenced via the instance name or self

>If an attempt is made to update a class variable using an instance name it will function as an instance variable for that instance

**Example**

```python
#Create class dog, this can be used to create multiple dog objects
class dog:
    'This class represents a dog'
    #Class variable or attribute name to hold the dogs name
    breed = 'Bulldog'

    #Creating a constructor which will be called everytime a new object is created
    def __init__(self):
        print('Dog Object created')

dog1 = dog()

#New instance variable name created for dog1
dog1.name = 'Rocky'
dog2 = dog()

#New instance variable name created for dog2
dog2.name = 'Rambo'

#Class variable breed is updated to Poodle, this will update in both instances
dog.breed = 'Poodle' \
            ''
print('Breed of Dog1 : ' + dog1.breed)
print('Name of Dog1 : ' + dog1.name)
print('Breed of Dog2 : ' + dog2.breed)
print('Name of Dog2 : ' + dog2.name)

```


# Exercises

**Write a python program to create dogs from a dog class and count the number of dogs created**

```python

#Create class dog, this can be used to create multiple dog objects
class dog:
    'This class represents a dog'
    #Class variable or attribute name to hold the dogs name
    breed = 'Bulldog'
    no_of_dogs = 0

    #Creating a constructor which will be called everytime a new object is created
    def __init__(self,name):
        print('Dog Object created')
        self.name = name
        dog.no_of_dogs = dog.no_of_dogs + 1



#Assert if no dog instances created
assert dog.no_of_dogs == 0, 'Number of dogs are not 0'

#Create dog1
dog1 = dog('Buddy')
#print no of dogs, should be 1
print('Number of dogs :', dog.no_of_dogs)

dog2 = dog('Bella')
#print no of dogs, should be 2
print('Number of dogs :', dog.no_of_dogs)

dog3 = dog('Max')
#print no of dogs, should be 3
print('Number of dogs :', dog.no_of_dogs)


```

**Create a class to define a car with the following :**
 - **The class should have atleast 1 class variable ( think of an    attribute which remains the same across all cars )**
-  **A car should require the attributes 'Make,Model,Year,Color, Engine'**
- **Create a method ‘start’ to start the car. When the method is called, the car’s ‘status’ attribute should be ‘ON’**
- **Create a method ‘accelerate’, which should take the argument speed. When the method is called the attribute ‘speed’ should    increase by the specified speed passed to the method**
- **Create a method ‘decelerate’, which should take the argument speed. When the method is called the attribute ‘speed’ should    decrease by the specified speed passed to the method**
- **Create a method ‘break’. When called the speed attribute should become 0**
- **Create a method ‘Off’. When called the car’s ‘status’ attribute should become 'OFF'**

**Rules to implement ( make use of try, except or if else statements ) :**
- **The car cant be started if its already ON**
- **The car cant accelerate, decelerate, break or turned OFF if its not ON**
- **Maximum speed of the car is 130**
- **The car cant decelerate if the speed is 0**
