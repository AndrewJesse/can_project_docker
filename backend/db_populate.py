import sqlite3
from datetime import datetime, timedelta

# Connect to the SQLite database
conn = sqlite3.connect('backend/can_project.db')
cursor = conn.cursor()

# Define the base data
base_arbitration_id = 'test_id'
base_data = 'test_data'
base_timestamp = datetime(2024, 7, 24, 0, 0, 0)

# Insert 20 rows of data
for i in range(20):
    arbitration_id = f'{base_arbitration_id}_{i+1}'
    data = f'{base_data}_{i+1}'
    timestamp = base_timestamp + timedelta(minutes=i)
    
    cursor.execute('''
        INSERT INTO can_messages (arbitration_id, data, timestamp) 
        VALUES (?, ?, ?)
    ''', (arbitration_id, data, timestamp))
    
    conn.commit()

# Close the connection
conn.close()

print("20 rows of dummy data inserted successfully.")
