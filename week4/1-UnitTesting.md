# Testing

> Testing is an integral part of software development

> Testing is the process of finding bugs, validating and verifying functionality in the software application

> Thorough testing is as important as coding itself

> Testing is done at multiple stages by developers, Quality Analysts, Business Analysts

**Types Of Testing**

> The most common categories of testing are :
> Unit Testing
> Integration Testing
> User Acceptance Testing

**Unit Testing**

> Unit testing is the most basic form of testing

> It is done by developers writing the code


**Integration Testing**

> Integration testing is done to test connectivity between different applications and systems

> Its usually at the application level

> It is done by developers or QA

**User Acceptance Testing**

> UAT is the end to end testing process involving multiple applications across multiple companies

> Done by Quality or Business Analysts


# Unit Testing

> Unit testing is the most basic form of testing

> It is done by developers writing the code

> In Unit Testing the smallest units of code are tested individually

> Each unit of code is tested for an expected output based on a given input or condition

> Unit Tests are usually automated

> Python provides a built in module for unit testing called unittest


**Example**

```python

#Import unittest module
import unittest

#Create a class by inheriting from unittest.TestCase
class UnitTestExample(unittest.TestCase):
    # Create a new test to test if 2+3 is 5
    def testAdditionOfNumbers(self):
        self.assertEqual(2+3,5)

#Running this will give you the result. Try it

```


**Eaxmple with multiple tests**

```Python

import unittest

#Define a function to convert inches to cm
def inchesToCm(inches):
    cm = inches * 2.54
    return cm




#Create the unit test class
class UnitTestExample(unittest.TestCase):


    #Create a test to check if upp() function works
    def testUpperCase(self):
        self.assertEqual('upper'.upper(),'UPPER')

    #Test the inchesToCm function we just created
    def testInchesToCm(self):
        self.assertEqual(inchesToCm(10),25.4)

```
