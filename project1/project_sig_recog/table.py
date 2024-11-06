import sqlite3

# Connect to the database or create it if it doesn't exist
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    signature BLOB
                )''')

# Insert student information
students_data = [
    ("Divyanshi", "C:/Users/divyanshi mittal/Desktop/student_data/signature1.jpg"),
    ("Harshit", "C:/Users/divyanshi mittal/Desktop/student_data/signature2.jpg"),
    ("Gautam", "C:/Users/divyanshi mittal/Desktop/student_data/signature3.jpg"),
    # Add more students as needed
]

for student_name, signature_file in students_data:
    with open(signature_file, "rb") as signature_blob:
        cursor.execute("INSERT INTO students (name, signature) VALUES (?, ?)",
                       (student_name, signature_blob.read()))

# Commit the changes and close the connection
conn.commit()
conn.close()
