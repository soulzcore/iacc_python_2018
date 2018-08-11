# SQLite

> SQLite is a disk based database which does not require a server to run

> SQLite can be used for storing data by applications without having to rely on an external database system

> SQLite supports the standard SQL Language

> SQLite is provided as a built in module in Python

> The name of the module is sqlite3


**Example - Create Table and insert records**

```Python

#import the sqlite3 module
import sqlite3

# Create a connection
conn = sqlite3.connect('example.db')

# Get a cursor to the DB
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE cars(make text, model text, trim text, year text)''')

# Insert a row of data
c.execute("INSERT INTO cars VALUES ('Ford','Explorer','Limited','2017')")

# Insert Multiple rows
c.execute("INSERT INTO cars VALUES ('BMW','X5','xDrive35D','2015'), ('Nissan','Altima','3.5SL','2016'), ('Toyota','Highlander','Limited','2017')")

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()


```



**Example - Retrieve data from the Sqlite databse**

```Python

import sqlite3

# Create a connection
conn = sqlite3.connect('example.db')

# Get a cursor to the DB
c = conn.cursor()


#Execute a Select all statement
c.execute('SELECT * FROM cars')

#Print all the records
print(c.fetchall())

#Select rows where make is Ford
c.execute('SELECT * FROM cars where make = "Ford"')

#Print the results
print(c.fetchall())

```
