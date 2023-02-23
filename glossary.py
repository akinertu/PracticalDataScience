# SQL and Built-in File Handling Modules in Python Ch3
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
#SQL (command line)z
    sqlite3 chinook.db #opens chinook db with SQLite shell
    .tables #prints out the tables in the database
    SELECT * FROM artists LIMIT 5; #selects all columns from artists 
#SQL (python)
    import sqlite3
        sqlite3.connect('chinook.db')
        connection = sqlite3.connect('chinook.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM artists LIMIT 5;')
        cursor.fetchall()
    
    