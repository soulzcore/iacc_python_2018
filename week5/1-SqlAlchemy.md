#Sql Alchemy

> SQL Alchemy is the Object Relationship Mapper for Python

> Object Relationship Mapping(ORM) is the technique of being able to create, query and manipulate data in SQl Databases ( or other data stores ) using Object Oriented programming principles

> Data in a SQL Database like ( sqllite, MySql, MSSql ) is stored in tables as columns and rows

> SQL queries are used to access and manipulate the data in the tables

> ORM is used when the programmer would like access the data in the relational tables as objects, just like objects they can have attributes and methods.

> Sql ALchemy converts the actions( methods ) you apply to objects to Sql behind the scenes

> In the ORM methodology, classes are created and mapped to tables in the database. So, if there is a table you would like to interact with, you will have to create a class which would map to the table and then utilize the methods provided by Sql Alchemy to interact with it. Example : Create new table, add rows, retrieve rows etc..

**SQL Alchemy Components**

> Sql Alchemy ORM framework consists of the following components



#Image
**Engine**
>  The starting point of the application

> **To use the engine with MS SQL server you will need pymssql package installed. Please follow the instructions here :**
https://docs.microsoft.com/en-us/sql/connect/python/pymssql/step-1-configure-development-environment-for-pymssql-python-development?view=sql-server-2017


```python
from sqlalchemy import create_engine

#For MS SQL Server
engine = create_engine('mssql+pymssql://username:password@localhost:1433')


#For SQLite
engine = create_engine('sqlite:///DBNAME.db')

```
> The engine accepts the DB connection string as one of the arguments

> When the connect method is called on the engine object using engine.connect(), the Engine will establish a connection from the connection pool

> Passing ```echo=True``` to create_engine will print out the SQL statements that are executed. This is useful for debugging

```python
from sqlalchemy import create_engine
engine = create_engine('mssql+pymssql://username:password@localhost:1433', echo=True)
```

**Pool**

> A connection pool is a cache or collection of database connections which are maintained and can be reused when a new connection request is made

> The Engine will ask the connection pool for a connection when the connect() or execute() methods are called

> The default size of the pool is 5

**Dialect**

> SQL Alchemy uses Dialects to connect to different DB systems

> SQL Alchemy ships with a few built in dialect for databases such as : MySQL, MS Sql, Oracle, Sqlite etc..

> Dialect interface with DBAPI's to interact and perform operations on DB's

**DBAPI**

> DBAPI stands “Python Database API Specification”.

> DBAPI is the standard Python specification to talk to DB's.

> Dialects are built on top of DBAPI's


**Connecting to MSSQL**

```python

# import create_engine from sqlalchemy module
from sqlalchemy import create_engine

# Create a new engine with the MSSQL dialect and pyodbc DBAPI and assign it to the variable engine
engine = create_engine('mssql+pymssql://username:password@localhost:1433', echo=True)

```

**Declarative base**

> The SQL Alchemy ORM consists of three main components: Table, Mapper and the class

> Table refers to the table in the database

> Mapper refers to the mapping between the table and the python class/object

> SQL Alchemy provides a declarative base which allows all of the three to be expressed at once

```Python

Base = declarative_base()

```

**Table Class**

> The table class will have attributes which will be directly mapped to the table columns in the DB

> Example : Consider the table named 'students', with the following columns : 'id, firstname, lastname, address'

> The table class( we will call it Student) can be written as follows :

```Python

# Student class inherits from the declarative_base(Base) class
class Student(Base):

    # This will be mapped to the table name  
    __tablename__ = "students"

    # The following class variables/attributes will be mapped to the column names
    id = Column(Integer, primary_key=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)

    # Constructor to populate values if supplied during object creation
    def __init__(self, username, firstname, lastname):

        self.username = username
        self.firstname = firstname
        self.lastname = lastname

```

**Creating tables**

> To create the students table if it does not exist in the DB using Sql Alchemy, run the following command :

```Python
Base.metadata.create_all(engine)

```

> The create_all method will create the table with the structure defined in the table class ( Students )

**Full Code**

```Python
# import create_engine from sqlalchemy module
from sqlalchemy import create_engine

# import the required types
from sqlalchemy import Column, Integer, String

#import the declarative_base
from sqlalchemy.ext.declarative import declarative_base

# Create a new engine with the MSSQL dialect and pyodbc DBAPI and assign it to the variable engine
engine = create_engine('mssql+pymssql://username:password@localhost:1433', echo=True)

#Create the declarative base
Base = declarative_base()

class Student(Base):

    # This will be mapped to the table name  
    __tablename__ = "students"

    # The following class variables/attributes will be mapped to the column names
    id = Column(Integer, primary_key=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)

    def __init__(self, username, firstname, lastname):

        self.username = username
        self.firstname = firstname
        self.lastname = lastname

# Create the table students
Base.metadata.create_all(engine)

```

> Running the above code will be the same as executing the following SQL :

```sql
CREATE TABLE Student (
	id INTEGER NOT NULL,
	username VARCHAR,
	firstname VARCHAR,
	lastname VARCHAR,
	PRIMARY KEY (id)
)

```



**Session**

> Session in general session is a temporary interaction or information exchange between systems

> The Sql Alchemy session holds all the objects and establishes connection with the DB

> The connection remains open until the session remains in effect.

> The connection is closed when the session ends

> Session is created and bound to the engine that was created by Sql Alchemy

> Once the session is created DB operations can be performed, like inserting and queries records.


**Usage**

```Python
# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()

```

**Some Session Methods**

> * add() : Add a new object(record) to the session
> * commit() : commit the session
> * close() : Close the session and delete all objects from the session memory


**Insert Records**

> New records can be inserted to the DB by creating a new object for record

> In the previous example, to insert student records into the DB, we need to create new student object with the corresponding values and add them to the session

> Committing the session will write the objects/records to the DB

**Example**

> Add a new student record to the DB with the following value :  
> * id : 123
> * firstname : James
> * lastname : bond

```python
james_bond = Student(123,"James","Bond")
session.add(james_bond)

# commit the record the database
session.commit()

```

> **Note : Ideally the Student class will be created in a separate file and imported into the code as a module and referenced from there**


**Full Code to insert multiple records**

```Python

# import create_engine from sqlalchemy module
from sqlalchemy import create_engine

# import the required types
from sqlalchemy import Column, Integer, String

# import the declarative_base
from sqlalchemy.ext.declarative import declarative_base

# import session maker
from sqlalchemy.orm import sessionmaker


# Create a new engine with the MSSQL dialect and pyodbc DBAPI and assign it to the variable engine
engine = create_engine('mssql+pymssql://username:password@localhost:1433', echo=True)

#Create the declarative base
Base = declarative_base()

# Create a new Student class which inherits from Base
class Student(Base):

    # This will be mapped to the table name
    __tablename__ = "students"

    # The following class variables/attributes will be mapped to the column names
    id = Column(Integer, primary_key=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)

    def __init__(self, username, firstname, lastname):

        self.username = username
        self.firstname = firstname
        self.lastname = lastname

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()


#Create 3 new students(objects) and add them to the session
james_bond = Student(123, "James", "Bond")
session.add(james_bond)

ethan_hunt = Student(124, "Ethan", "Hunt")
session.add(ethan_hunt)

john_wick = Student(125, "John", "Wick")
session.add(james_bond)

# commit the record the database
session.commit()




```


 **Quering the DB**

> The DB can be queries using the query() method of the session object

> The query method returns an iterable with the records returned as objects

> The column values can be accessed via attributes of the object returned

**Example**

```python

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a new engine with the MSSQL dialect and pyodbc DBAPI and assign it to the variable engine
engine = create_engine('mssql+pymssql://username:password@localhost:1433', echo=True)

#Create the declarative base
Base = declarative_base()

class Student(Base):

    # This will be mapped to the table name
    __tablename__ = "students"

    # The following class variables/attributes will be mapped to the column names
    id = Column(Integer, primary_key=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)

    def __init__(self, username, firstname, lastname):

        self.username = username
        self.firstname = firstname
        self.lastname = lastname

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()

# Query for objects in the Student DB and print them out
for student in session.query(Student):
    print(student.firstname, student.lastname)


```

> To filter records, session provides additional methods like 'filter'

**Example**


```python

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a new engine with the MSSQL dialect and pyodbc DBAPI and assign it to the variable engine
engine = create_engine('mssql+pymssql://username:password@localhost:1433', echo=True)

#Create the declarative base
Base = declarative_base()

class Student(Base):

    # This will be mapped to the table name
    __tablename__ = "students"

    # The following class variables/attributes will be mapped to the column names
    id = Column(Integer, primary_key=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)

    def __init__(self, username, firstname, lastname):

        self.username = username
        self.firstname = firstname
        self.lastname = lastname

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()

# Query for objects in the Student DB and print them out
for student in session.query(Student).filter(Student.firstname == 'James'):
    print(student.firstname, student.lastname)


```
