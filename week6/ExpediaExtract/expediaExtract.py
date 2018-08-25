import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Import sendMail and sqliteTool modules
from week6 import sendMail, sqliteTool


#Chrome Driver Location and expedia URL
path_to_chromedriver = '/Users/mohammed/Downloads/chromedriver'
url = 'https://www.expedia.com/Hotels'

#Search Details a
destination = 'NYC'
checkin_date = '09/22/2018'
checkout_date = '09/25/2018'


#Generate Current Date
current_date = time.strftime("%m/%d/%Y")

#Create variables required for sending an E-Mail
from_email = 'soulzcore@gmail.com'
to_email = 'soulzcore@gmail.com'
subject = 'Expedia Hotel Prices'
body = 'Check the attachment'
fileName = 'hotels.csv'

#Create variables for writing to SQLITE
db_name = 'hotels.db'
table_name = 'expedia'

#Initialize the Chrome web driver
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

#Open the Expedia URL
browser.get(url)

#Find the destination field and enter NYC as the input
browser.find_element_by_xpath('//*[@id="hotel-destination-hlp"]').send_keys(destination)

#Find the Checkin date field and clear it
browser.find_element_by_xpath('//*[@id="hotel-checkin-hlp"]').clear()

#Enter checkin date
browser.find_element_by_xpath('//*[@id="hotel-checkin-hlp"]').send_keys(checkin_date)

#Clear the checkout date field and enter teh checkout date
browser.find_element_by_xpath('//*[@id="hotel-checkout-hlp"]').clear()

for x in range(10):
    browser.find_element_by_xpath('//*[@id="hotel-checkout-hlp"]').send_keys(Keys.BACK_SPACE)

print('here')

browser.find_element_by_xpath('//*[@id="hotel-checkout-hlp"]').send_keys(checkout_date)

browser.find_element_by_xpath('//*[@id="hotel-checkout-hlp"]').send_keys(Keys.ENTER)

#browser.find_element_by_xpath('//*[@id="hotel-checkout-hlp"]').send_keys(checkout_date)

#Find and click the Submit button
#browser.find_element_by_xpath('//*[@id="gcw-hotel-form-hlp"]/div[9]/label/button').click()

#Wait for expedia to load results or for 20 seconds whichever comes first
try:
    wait = WebDriverWait(browser, 20)
    #Wait until the the hotelResultTitle is detected on the page
    element = wait.until(EC.presence_of_element_located((By.ID,'hotelResultTitle')))
except:
    print('Error - Unable to find results')

#create a list to store hotel details
hotels_list = []

#Create a page number variable and default it to 1, this will be incremented at every page load
page_no = 1

#Create a variable to identify if the next button is disabled ( the last page )
next_button_disabled = False

#Create a loop to iterate until next button becomes disabled(next_button_disabled becomes true on the last page)
while not next_button_disabled:
    #Print the current page number
    print('Current Page Number : ', page_no)

    #Find all tags name article on the current page. The article tag contains hotel details
    hotels = browser.find_elements_by_tag_name('article')

    #Iterate over the list of Hotels(articles) on the current page
    for hotel in hotels:

        #Try to find the hotel name price, if there is an error print 'Encountered Error' and go to the next hotel
        try:

            #Get the hotel name
            hotel_name = hotel.find_element_by_class_name('visuallyhidden').text

            #Get the hotel price
            hotel_price =  hotel.find_element_by_class_name('actualPrice').text

            #Create a tuple with the hotel name, price and todays date.
            hotel_tuple = (hotel_name,hotel_price, current_date)

            #Add the tuple to the hotels_list variable which was created earlier
            hotels_list.append(hotel_tuple)

        except:

            print('Encountered error')


    #Get the next button disabled status, this will be true if the next button is disabled else false
    next_button_disabled = browser.find_element_by_class_name('pagination-next').get_attribute('disabled')

    if not next_button_disabled:

        #increment the page number
        page_no = page_no + 1

        #Click next button on the page
        browser.find_element_by_class_name('pagination-next').find_element_by_tag_name('abbr').click()

        #Wait 5 seconds, this is to let expedia load new results from the next page
        time.sleep(5)



#Create a data frame from the hotel list
hotel_df = pd.DataFrame(hotels_list, columns=['name','price','date']).drop_duplicates()

#Print the number of rows and columns in the data frame
print(hotel_df.shape)

#Print the descriptive statistics of the data frame
print(hotel_df.describe())

#Write the dataframe data into a csv file
hotel_df.to_csv(fileName,index=False, encoding='utf8')

#Write the results of the data frame to a DB by calling the writeToDB function from the sqliteTool module
sqliteTool.writeToDB(hotel_df, db_name, table_name)

#Send E-Mail with the csv as an attachment by calling the sendMail function of the sendMail module
sendMail.sendMail(from_email, to_email, subject, fileName)
