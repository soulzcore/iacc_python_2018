import sqlite3

#Define a function to accept a data frame, database name and a table name as inputs and write the dataframe to SQLITE
def writeToDB(df,db_name,table_name):

    #Create a new connection to the db name provided in the input
    con = sqlite3.connect(db_name)

    #Write the data frame to the DB
    df.to_sql(table_name, con, if_exists='append', index=False)

    #close the connection
    con.close()
