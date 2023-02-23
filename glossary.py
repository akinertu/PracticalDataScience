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
        
    
    