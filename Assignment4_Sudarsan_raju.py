
# coding: utf-8

# In[37]:


import csv
import pyodbc

#open csv file and set up csv reader
csv_file = open('walmart-comment-data.csv', 'r', encoding='utf-8-sig')
csv_reader = csv.DictReader(csv_file)


# In[69]:



#establish database connection and generate cursor
cs = "DRIVER={/usr/local/mysql-connector-odbc-8.0.12-macos10.13-x86-64bit/lib/libmyodbc8a.so};SERVER=localhost;port=3306;DATABASE=facebook;USER=root;PASSWORD=password;charset=utf8mb4"
connection = pyodbc.connect(cs)
connection.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
connection.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
connection.setencoding(encoding='utf-8')
csr = connection.cursor()


# In[72]:


#load data to database
query = 'INSERT INTO fb_comments VALUES(?,?,?,?,?,?,?);';
for record in csv_reader:
    args = (record['page_id'], record['post_id'], record['comment_id'], record['creation_timestamp'], record['user_name'], record['user_id'], record['comment_text'])
    try:
        csr.execute(query, args)
    except pyodbc.IntegrityError:
        continue


# In[67]:


#commit changes and close connection
connection.commit()
connection.close()

