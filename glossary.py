#Built-in File Handling Modules in Python Ch3
    with open('reading.json', 'w') as f:
            text = f.read()
#JSON module (JavaScript Object Notation)
    import json
        json.dumps(data_dictionary) #convert dict to a JSON-format string
        json.loads(json_string) #convert a JSON-format string to dict
        json.dump(data_dictionary, f) #save JSON data to a text file
    import credentials as creds #Saving credentials or data in a Python file
        creds.username
        creds.password
    import pickle as pk #Saving Python objects
        with open('readings.pk', 'rb') as f: #Opening Python objects
#SQL commands (command line)z
    sqlite3 chinook.db #opens chinook db with SQLite shell
    .tables #prints out the tables in the database
    SELECT * FROM artists LIMIT 5; #selects all columns from artists
    SELECT Total, InvoiceDate FROM invoices ORDER BY Total DESC LIMIT 5;
    SELECT Total, BillingCountry FROM invoices WHERE BillingCountry == "Canada" LIMIT 5;
    WHERE BillingCountry LIKE "%can%" #strings that contain the letters c, a, and n
    GROUP BY BillingCountry ORDER BY SUM(Total) DESC 
    JOIN tracks ON tracks.TrackId = invoice_items.TrackId
    COUNT(invoice_items.TrackId)
#SQL (python)
    import sqlite3
        sqlite3.connect('chinook.db')
        connection = sqlite3.connect('chinook.db') #chinook.db file will be created if it does not exist. 
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM artists LIMIT 5;') #enter SQLite commands to execute
        cursor.fetchall() #retrieve all the results from the query
        connection.close() #not necessarily required, but will make our code moreexplicit
    from sqlalchemy import create_engine
        engine = create_engine('sqlite:///book_sales.db')
        connection = engine.connect()
        result = connection.execute("select * from book_sales")
        connection.close()
        
        with engine.connect() as connection: #automatically close the database connection when we're out of the with block:
            result = connection.execute("select * from book_sales")
            for row in result:
                print(row)
    