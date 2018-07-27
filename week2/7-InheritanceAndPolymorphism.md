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


# Multiple Inheritance

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
