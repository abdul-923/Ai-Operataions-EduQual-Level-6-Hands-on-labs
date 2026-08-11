

##Creating a Table in SQLite

import sqlite3

connection = sqlite3.connect(':memory:')

cursor = connection.cursor()
cursor.execute("""

CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  grade REAL

)
""")


##Inserting Data into the Table
students_data = [
    (1, 'Alice', 85.5),
    (2, 'Bob', 78.0),
    (3, 'Charlie', 92.0)
]


cursor.executemany("INSERT INTO students VALUES (?, ?, ?)", students_data)
connection.commit()


##Querying Data

cursor.execute("SELECT * FROM students")
results = cursor.fetchall()


for row in results:
    print(row)


connection.close()
