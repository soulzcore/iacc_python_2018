# USE CASE – DALLAS CITY CRIME ANALYSIS


**Dataset details**

> The Dallas police incidents is a publicly available dataset which has incident reports from 2014 to 2017

> The Dataset can be downloaded in csv format from : https://www.dallasopendata.com/api/views/tbnj-w5hb/rows.csv?accessType=DOWNLOAD

> The Metadata can be found at https://www.dallasopendata.com/Public-Safety/Police-Incidents/tbnj-w5hb?defaultRender=table


**Questions**

> Find the number of rows and columns in the dataset

> Find the top 5 offences reported and their count

> Find the average time taken to send a dispatch after receiving the incident report

> Find the top 5 longest dispatch times ( time between receiving a call and sending out a dispatch )

> Find the 10%, 25%, 50% and 80% percentile of dispatch times


**Solution**

```Python


import pandas as pd

# Create a variable with the csv filename we would like to analyze
filename = '/Users/mohammed/Downloads/Police_incidents.csv'

# Create a data frame from the csv file
df = pd.read_csv(filename,header=0, index_col = False)


# Print All columns in the csv file as list
print(df.columns.values.tolist())



# Create a new dataframe df1 from selected columns of interest from the original df
df1 =  df[['Year of Incident','Type of Incident','Call (911) Problem','Type of Location','Type of Property','Incident Address','Zip Code','City','State','Date of Report','UCR Offense Name','Call Received Date Time','Call Dispatch Date Time']]


# Number of columns in the new dataframedf1
print('Number of Columns : ' , len(df1.columns))


# Print All columns as list in df1
print(df1.columns.values.tolist())


# Number of rows in df1
print('Number of rows :' , len(df1))

# Print default metrics of df1
print(df1.describe())

# type function can be used to determine the datatype. It should be dataframe
print(type(df1))



# Find all unique incidents in the dataset
incident_types = df1['UCR Offense Name'].unique()

# Number of Unique type of incidents
print('Number of unique incident types', len(incident_types))


# Create a new dataframe inc_group by Grouping incidents and calculating the number or size of each type of incident, rename the index to count
inc_group =  df1.groupby('UCR Offense Name').size().reset_index(name='count')


# Sort the new dataframe in descending order, highest number incidents first
inc_group = inc_group.sort_values('count', ascending=False)


# Print the top 5 incidents
print('\n\n------ The Top 5 incidents ----- \n\n')
print(inc_group.head(5))


# Create a new column  from the Call Received time column of df1 and convert strings into DateTime object
df1['Call Received Date Time'] = pd.to_datetime(df1['Call Received Date Time'])




# Create a new column from the Call Dispatch time column of df1 and convert strings into DateTime object
df1['Call Dispatch Date Time'] = pd.to_datetime(df1['Call Dispatch Date Time'])


# Calculate time between call received and call dispatched, this will be in days
df1['Time to Dispatch'] = (df1['Call Dispatch Date Time'] - df1['Call Received Date Time'])


# Convert the time to dispatch column into hours, sort and save it as a new series
time_to_dispatch =  df1['Time to Dispatch'].apply(lambda x: x.total_seconds()/60.0 / 60.0).sort_values(ascending=False)


# Print the longest 5 dispatch times
print('\n\n------ The 5 longest dispatch times are ----- \n\n')
print(time_to_dispatch.head(5))


# Print descriptive statics with the top 10%, 25%, 50% and 80% percentiles
print('\n\n------ Descriptive statistics with the top 10, 25, 50 and 80 percentiles ----- \n\n')
print(time_to_dispatch.describe(percentiles = [.10, .25, .50, .80]))


```
