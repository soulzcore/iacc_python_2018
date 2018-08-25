# Exploring the Dallas Police Incidents Dataset

**Example - Time Series plot of number of incidents in the last 4 years**


```python

import pandas as pd
import matplotlib.pyplot as plt


# Create a variable with the csv filename we would like to analyze
filename = '/Users/mohammed/Downloads/Police_incidents.csv'

# Create a data frame from the csv file
df = pd.read_csv(filename,header=0, index_col = False)

# Create a new dataframe df1 from selected columns of interest from the original df
df1 =  df[['Year of Incident','Type of Incident','Call (911) Problem','Type of Location','Type of Property','Incident Address','Zip Code','City','State','Date of Report','UCR Offense Name','Call Received Date Time','Call Dispatch Date Time']]


# Create a new dataframe inc_group by Grouping incidents and calculating the number or size of each type of incident, rename the index to count
inc_group =  df1.groupby('Date of Report').size().reset_index(name='count')


# Sort the new dataframe in descending order, highest number incidents first
inc_group = inc_group.sort_values('count', ascending=False)

#Print the top 5
print(inc_group.head(5))

#Plot the dataframe
inc_group.plot(x='Date of Report', y='count')


#Render it via PyCharm
plt.show()


```



**Example - Time Series plot of selected multiple incidents**

```python

import pandas as pd
import matplotlib.pyplot as plt



# Create a variable with the csv filename we would like to analyze
filename = '/Users/mohammed/Downloads/Police_incidents.csv'

# Create a data frame from the csv file
df = pd.read_csv(filename,header=0, index_col = False)

# Create a new dataframe df1 from selected columns of interest from the original df
df1 =  df[['Year of Incident','Type of Incident','Call (911) Problem','Type of Location','Type of Property','Incident Address','Zip Code','City','State','Date of Report','UCR Offense Name','Call Received Date Time','Call Dispatch Date Time']]

#Convert Call Received Date Time to date time object
df1['Date of Report'] = pd.to_datetime(df1['Call Received Date Time'])

#Replace with just the date and not the time
df1['Date of Report'] = df1['Date of Report'].apply(lambda x: x.date())


#Create a new data frame with the Date Of Report and the UCR Offense Name
dfp = df1[['Date of Report','UCR Offense Name']]



#Group by Date and count number of ocurrances of unique incidents and pivot table
dfp = pd.pivot_table(dfp,index='Date of Report',columns='UCR Offense Name',aggfunc=len, fill_value=0)

#Slice only 4 incident types
dfp = dfp[['THEFT/BMV','ACCIDENT MV', 'BURGLARY-RESIDENCE', 'ASSAULT']]


#Plot the data frame
dfp.plot()


#Render the plot in PyCharm
plt.show()

```



**Example - Time Series plot of selected multiple incidents between Jan 2018 to Aug 2018**


```python

import pandas as pd
import matplotlib.pyplot as plt



# Create a variable with the csv filename we would like to analyze
filename = '/Users/mohammed/Downloads/Police_incidents.csv'

# Create a data frame from the csv file
df = pd.read_csv(filename,header=0, index_col = False)

# Create a new dataframe df1 from selected columns of interest from the original df
df1 =  df[['Year of Incident','Type of Incident','Call (911) Problem','Type of Location','Type of Property','Incident Address','Zip Code','City','State','Date of Report','UCR Offense Name','Call Received Date Time','Call Dispatch Date Time']]

#Convert Call Received Date Time to date time object
df1['Date of Report'] = pd.to_datetime(df1['Call Received Date Time'])

#Replace with just the date and not the time
df1['Date of Report'] = df1['Date of Report'].apply(lambda x: x.date())


#Create a new data frame with the Date Of Report and the UCR Offense Name
dfp = df1[['Date of Report','UCR Offense Name']]



#Group by Date and count number of ocurrances of unique incidents and pivot table
dfp = pd.pivot_table(dfp,index='Date of Report',columns='UCR Offense Name',aggfunc=len, fill_value=0)

#Slice only 4 incident types
dfp = dfp[['THEFT/BMV','ACCIDENT MV', 'BURGLARY-RESIDENCE', 'ASSAULT']]


#Create Start and End Date variables
startdate = pd.to_datetime("2018-01-01").date()
enddate = pd.to_datetime("2018-08-01").date()

#Filter the data frame to select rows between the start and the end date
dfp = dfp.loc[startdate:enddate]


#Plot the data frame
dfp.plot()


#Render the plot in PyCharm
plt.show()

```



**Example - Analysis by day of the week**

```python

import pandas as pd
import matplotlib.pyplot as plt



# Create a variable with the csv filename we would like to analyze
filename = '/Users/mohammed/Downloads/Police_incidents.csv'

# Create a data frame from the csv file
df = pd.read_csv(filename,header=0, index_col = False)

# Create a new dataframe df1 from selected columns of interest from the original df
df1 =  df[['Year of Incident','Type of Incident','Call (911) Problem','Type of Location','Type of Property','Incident Address','Zip Code','City','State','Date of Report','UCR Offense Name','Call Received Date Time','Call Dispatch Date Time']]

#Convert Call Received Date Time to date time object
df1['Date of Report'] = pd.to_datetime(df1['Call Received Date Time'])

#Replace with just the date and not the time
df1['Date of Report'] = df1['Date of Report'].apply(lambda x: x.weekday())


#Create a new data frame with the Date Of Report and the UCR Offense Name
dfp = df1[['Date of Report','UCR Offense Name']]



#Group by Date and count number of ocurrances of unique incidents and pivot table
dfp = pd.pivot_table(dfp,index='Date of Report',columns='UCR Offense Name',aggfunc=len, fill_value=0)

#Slice only 4 incident types
dfp = dfp[['THEFT/BMV','ACCIDENT MV', 'BURGLARY-RESIDENCE', 'ASSAULT']]




#Plot the data frame
dfp.plot(kind='bar')


#Render the plot in PyCharm
plt.show()

```



**Example - Zip Code analysis**

```python

import pandas as pd
import matplotlib.pyplot as plt


#pd.set_option('display.max_columns', 500)


# Create a variable with the csv filename we would like to analyze
filename = '/Users/mohammed/Downloads/Police_incidents.csv'

# Create a data frame from the csv file
df = pd.read_csv(filename,header=0, index_col = False)

# Create a new dataframe df1 from selected columns of interest from the original df
df1 =  df[['Year of Incident','Type of Incident','Call (911) Problem','Type of Location','Type of Property','Incident Address','Zip Code','City','State','Date of Report','UCR Offense Name','Call Received Date Time','Call Dispatch Date Time']]

#Convert Call Received Date Time to date time object
df1['Date of Report'] = pd.to_datetime(df1['Call Received Date Time'])


# Create a new dataframe inc_group by Grouping incidents and calculating the number or size of each type of incident, rename the index to count
inc_group =  df1.groupby('Zip Code').size().reset_index(name='count')


# Sort the new dataframe in descending order, highest number incidents first
inc_group = inc_group.sort_values('count', ascending=False)


inc_group.set_index('Zip Code', inplace=True)

#Print the top 5
#print(inc_group.head(5))

#Plot the dataframe
inc_group.plot(kind='pie', y='count')


#Render it via PyCharm
plt.show()


```
