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
# Pandas & Numpy ch4
    !pygmentize -l text data/data.csv #print csv text
    import pandas as pd
        pd.read_csv('data.csv') # read csv file
        pd.read_excel('data.xlsx', engine='openpyxl') # read excel file
        with engine.connect() as connection:
            pd.read_sql_query(query, connection) # read SQLite database
        df.head() .tail() .index .columns .info() .shape
        pd.concat([df1, df2, df3], axis=1, join=inner) #join along the columns, only rows with a matching index are joined.
        pd.merge()
        df.iloc[0] #first row by indexing
        df.iloc[-1] #last row by indexing
        df.iloc[0, 0] #first column of first row by indexing
        df.iloc[-1, -1] #last column of last row by indexing
        df.loc[3502] #rows with the index value of 3502
        df.reset_index(inplace=True, drop=True) # resets the index to a sequential RangeIndex
        pd.read_csv('csvfile.csv', skiprows=5) #to skip the first 5 rows
        df = df.iloc[:-5] # removing the last 5 rows.
        df[['col1', 'col2']] #selecting a column
        df.append(datarow)
        df.isna().sum() #the counts of missing values
        df.notna() df.notnull() df.isnull()
        df.describe() #statistics
        df['col1'].mode() # most frequent value
        df['col1'].value_counts() #how many times each unique value appears
        df['col'].unique().shape #number of unique values
        df.corr() #DataFrame of correlation results (Pearson correlation)
        df[df['col'] > 4e6] # filtering by mask
        df[df['col1'] != 'value1'] #rows that are not value1
        df[itunes_df['col1'].str.contains('asd..')] #rows contains asd
        df.drop('col2', axis=1, inplace=True) # remove col2
        itunes_df[~itunes_df['col1'].isin(['val1 ', 'val2', 'val3'])] #values with values val1 val2 val3 excluded
        df.dropna(inplace=True) #drop the rows with missing values
        df.loc[df['col1'].isna(), 'col1'] = 'Unknown' #ill the missing values with a specific value
        df['col1'].fillna('Unknown', inplace=True)
        df['col1'].fillna(df['col1'].mode(), inplace=True) #fill the missing values with mode of column
    import matplotlib.pyplot as plt
        df['col1'].hist(bins=30)
        plt.show()
        df.plot.scatter(x='col1', y='col2') #scatter plot
        df['col1'].value_counts().plot.bar() #bar plot
        df[df['col1'] > 2e6]['col2'].value_counts() # counts of col2 value while col1 > 2e6
        df.set_index('col1', inplace=True)
        df['col2'].plot(logy=True) #plot and using a logarithmic scale
    #KNN (k-nearest neighbors) imputation
    import numpy as np
        df.loc[0, 'Bytes'] = np.nan
    from sklearn.impute import KNNImputer
        imputer = KNNImputer()
        imputer.fit_transform(df [['col1', 'col2', 'col3']])  #takes in data with missing values, 
        #fits a KNN model, and then fills in the missing values with predictions from the model
        df['col2'] = imputed[:, 1] #all rows and the second column
    #IQR method to detect outliers
        def remove_outliers(df, column):
            q1 = df[column].quantile(0.25)
            q3 = df[column].quantile(0.75)
            iqr = q3 - q1
            upper_boundary = q3 + 1.5 * iqr
            lower_boundary = q1 - 1.5 * iqr
            new_df = df.loc[(df[column] > lower_boundary) & \
                                (df[column] < upper_boundary)]
        return new_df
        df_clean = remove_outliers(df, 'column')
    #Duplicate values, transform data
        df.duplicated().sum() #check for duplicates
        df.drop_duplicates(inplace=True) #drop duplicated rows
        df['col1'] = itunes_df['col1'].astype('int') # convert column datatype to integer
        df['Genre'].replace({'metal': 'Metal', 'met': 'Metal'})
        df['col1'].str.lower() #lowercasing strings
        df.groupby('col1').mean()['col2'].sort_values().head()
        pd.to_datetime(df['time'], unit='ms') #convert the time column to a pandas datetime datatype:
    # Saving Dataframes to disc
        df.to_csv('data/filename.csv', index=False)
        df.to_excel('data/filename.csv')
        