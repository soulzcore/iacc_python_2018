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

1) **Write a python program to create dogs from a dog class and count the number of dogs created**

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

2) **Create a class to define a car with the following :**
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


# Inheritance

> Object-oriented programming allows classes to inherit commonly used state and behavior from other classes

> This technique is called inheritance

> In inheritance there is usually a parent class from which multiple child classes can inherit

> The child classes will get almost all of the features from the parent class

> Lets consider Animal is a parent class
> Animal has attributes : color, breed, name, isPet etc..
> Animal has methods : eat(), sleep(), walk(), makeNoise()

> Lets consider a child class Dog which is inherited from Animal
> Dog will have the same attributes and methods as the class Animal, without them being explicitly defined in Dog class

> Lets consider another child class Cat which is inherited from Animal
> Cat will have the same attributes and methods as the class Animal, without them being explicitly defined in Dog class


**Usage**

```python
class ParentClass()
    init;
    attributes;
    methods;

class childClass(ParentClass)
    init;

```



**Example**

```python
#Create an Animal Class
class Animal():
    'This is a Parent class for creating Animals'

    def __init__(self,name,breed,color):
        self.name = name
        self.breed = breed
        self.color = color


    def walk(self):
        print(self.name + ' is walking')

    def eat(self):
        print(self.name + ' is eating')

    def makeNoise(self):
        print(self.name + ' is making noise')

class Dog(Animal):
    'This is the Dog class inherited from Animal'

    '''The keyword pass is used when you do not have any statements or expressions.
      In this case Dog will inherit everything from the animal class so we dont need any code here, just the class'''

    pass

class Cat(Animal):
    'This is the cat class inherited from Animal'
    pass


#Create a new Dog object dog1
dog1 = Dog('max','bulldog','black')

#Create a new Cat object cat1
cat1 = Cat('manny','tabby','orange')

dog1.eat()
cat1.eat()
dog1.makeNoise()
cat1.makeNoise()

```

# Method overriding:

> Changing the functionality of a method in a Child Class inherited from a Parent class is called overriding

> Example : Animal Class has a method makeNoise(). Dogs bark and cats meow.

> makeNoise() can be overridden in the Dog class to make the dog bark and in the cat class to make the cat meow


**Example ( same as the one from last slide but updated Dog and Cat classes )**

```python
# Example

#Create an Animal Class
class Animal():
    'This is a Parent class for creating Animals'

    def __init__(self,name,breed,color):
        self.name = name
        self.breed = breed
        self.color = color


    def walk(self):
        print(self.name + ' is walking')

    def eat(self):
        print(self.name + ' is eating')

    def makeNoise(self):
        print(self.name + ' is making noise')

class Dog(Animal):
    'This is the Dog class inherited from Animal'

    #Override the makeNoise method to make the dog bark
    def makeNoise(self):
        print(self.name + ' is barking')

class Cat(Animal):
    'This is the cat class inherited from Animal'

    # Override the makeNoise method to make the cat meow
    def makeNoise(self):
        print(self.name + ' is meowing')


#Create a new Dog object dog1
dog1 = Dog('max','bulldog','black')

#Create a new Cat object cat1
cat1 = Cat('manny','tabby','orange')

dog1.eat()
cat1.eat()
dog1.makeNoise()
cat1.makeNoise()


```


**Multiple Inheritance**

> A class can inherit from multiple classes

> This is called Multiple Inheritance

> If a method exists in multiple methods Python looks from classes left to right to find the first matched method

**Usage**

```python

class ParentClass1()
    init;
    attributes;
    methods;

class ParentClass2()
    init;
    attributes;
    methods;


class childClass(ParentClass1,ParentClass2)
    init;

```


**Example**

```python
class ClassicPhone:
    'Classic phones are old school phones, which can only be used for phone calls'
    def __init__(self,make,model):
      self.make = make
      self.model = model

    def makePhoneCall(self):
      print('Calling')

    def receivePhoneCall(self):
      print('Receiving')

class Camera:
    'Cameras are used to take pictures'
    def __init__(self,make,model):
      self.make = make
      self.model = model

    def takePicture(self):
      print('Taking Picture')

class CameraPhone(ClassicPhone,Camera):
    'New generation phones with inbuilt camera'
    def __init__(self,make,model):
      self.make = make
      self.model = model

#Create a new iphone 6 object from CameraPhone class
iphone6 = CameraPhone('Apple', 'iphone')
#Call MakePhoneCall method
iphone6.makePhoneCall()
#Call Receive Phone Call method
iphone6.receivePhoneCall()
#Call Take Picture Method
iphone6.takePicture()

```


# Polymorphism

> Polymorphism in OOP is the ability to refer to multiple objects by a single generic object

> The generic object is usually the parent class which can be used to refer to any of the objects created by the child class

**Example**

```python
#Create an Animal Class
class Animal():
    'This is a Parent class for creating Animals'

    def __init__(self,name,breed,color):
        self.name = name
        self.breed = breed
        self.color = color


    def walk(self):
        print(self.name + ' is walking')

    def eat(self):
        print(self.name + ' is eating')

    def makeNoise(self):
        print(self.name + ' is making noise')

class Dog(Animal):
    'This is the Dog class inherited from Animal'

    # Override the makeNoise method to make the dog bark
    def makeNoise(self):
        print(self.name + ' is barking')


class Cat(Animal):
    'This is the cat class inherited from Animal'

    # Override the makeNoise method to make the cat meow
    def makeNoise(self):
        print(self.name + ' is meowing')


# Create a new Dog object dog1
dog1 = Dog('max', 'bulldog', 'black')

#Create a new Cat object cat1
cat1 = Cat('manny','tabby','orange')

#Adding dog1 and cat1 to a list names animals
animals = [dog1,cat1]

#Iterating over the list of animals and calling the makeNoise method
for animal in animals:
    animal.makeNoise()

```
