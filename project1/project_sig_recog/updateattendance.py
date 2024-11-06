import sqlite3

# Create or connect to the SQLite database
conn = sqlite3.connect(
    r"C:\Users\divyanshi mittal\Desktop\projects\project1\project_sig_recog\attendance.db")
cursor = conn.cursor()

# Define the table to store attendance records
cursor.execute('''
CREATE TABLE IF NOT EXISTS attendance (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT,
    signature_match BOOLEAN
)
''')

# Commit changes and close the database connection
conn.commit()
conn.close()

# List of student names
student_names = ["Divyanshi", "Harshit", "Gautam"]

# Simulate a signature match for each student (1 for match, 0 for no match)
signature_matches = [0, 0, 0]

# Connect to the database
conn = sqlite3.connect(
    "C:/Users/divyanshi mittal/Desktop/project/attendance.db")
cursor = conn.cursor()

# Function to update attendance for a student


def update_attendance(student_name, signature_matched):
    cursor.execute('''
    INSERT INTO attendance (student_name, signature_match)
    VALUES (?, ?)
    ''', (student_name, signature_matched))

    # Commit changes to the database
    conn.commit()


# Initialize a flag to check if any student has a matching signature
student_with_match = False

# Update attendance for each student based on the signature match
for student_name, signature_match in zip(student_names, signature_matches):
    if signature_match == 1:
        update_attendance(student_name, True)
        student_with_match = True
    else:
        update_attendance(student_name, False)

# If no student has a matching signature, mark the first student as present
if not student_with_match:
    update_attendance(student_names[0], True)

# Query and display the attendance status for all students
cursor.execute('SELECT * FROM attendance')
records = cursor.fetchall()

for record in records:
    student_id, student_name, signature_match = record
    if signature_match:
        print(f"{student_name} is present")
    else:
        print(f"{student_name} is absent")

# Close the database connection
conn.close()
