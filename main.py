import sqlite3
conn = sqlite3.connect('store')
print ("Database has been created")

conn.execute("DROP TABLE IF EXISTS pet")

conn.execute("CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), checkups SMALLINT UNSIGNED, birth DATE, death DATE)")

print ("Table created successfully")

"INSERT INTO pet VALUES (1, 'Fluffy', 'Alice', 'cat', 'f', 5, '2001-02-04', null)"