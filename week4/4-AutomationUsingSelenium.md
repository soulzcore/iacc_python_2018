# WEB AUTOMATION FRAMEWORK - SELENIUM

**Selenium**

> Selenium is a framework which can be used to automate tasks that require a web browser

> Think accessing information on websites, filling out forms, navigating web pages etc..

> It is widely used for testing web application and for QA puposes

> It can also used for scraping information from the web.

> Selenium supports most of the popular browsers eg : Chrome, Firefox etc…

> Selenium provides an ide which can be installed as a plugin on the browser. It can be used to generate selenium scripts

> Selenium also provides API or a framework in multiple languages including Python, Java, C#, R etc..

> The Selenium API can be used to programatically control browsers

**Web Drivers**

> Webdriver is an API or framework which is used to driver browsers programmatically just like a real user

> Different browser vendors support their webdrivers

> Example : Google provides the chrome driver which can be used to drive the google chrome browser


**Installation**

> Selenium can be installed from pypi using pip. Run the following command in the command prompt:

``` pip install selenium
```


**Download Chrome Driver**

> Download chrome driver for your OS from here https://chromedriver.storage.googleapis.com/index.html?path=2.41/

> Unzip the zip to extract the chromedriver.exe file

> This will be the driver



**Example**

```Python
#Running this example will open a new chrome window, go to expedia.com/hotels and enter Dallas in the destination field

#Import Selenium webdriver
from selenium import webdriver

#Define the path to the downloaded chromedriver
path_to_chromedriver = '/Users/mohammed/Downloads/chromedriver'


#Create a new Webdriver and call it browser
browser = webdriver.Chrome(executable_path = path_to_chromedriver)


#URL that will be opened
url = 'https://www.expedia.com/Hotels'

#Open the URL
browser.get(url)


#Find the destination element's XPATH
destination = browser.find_element_by_xpath('//*[@id="hotel-destination-hlp"]')

#Enter Dallas in the destination field
destination.send_keys('Dallas')

```


**Common WebDriver Methods**

> find_element_by_name(var) – Find the HTML element with the attribute name is var

> find_element_by_xpath(xpath) – Find the element which matches the given xpath

> send_keys(var) – Enter var in the selected field

> click() – Click the selected element
