from sqlite3 import *

event_data = ['test', 'test', 'test', 'test', 'test']

connection = connect(database = 'bookings.db')
# Get a cursor on the database
bookings_db = connection.cursor()
# sql query to add the appropriate data to the tickets_bought table in the database
bookings_db.execute(
    "INSERT INTO tickets_bought SELECT " + "'" + event_data[0] + "', '" + event_data[1] + "', '" + event_data[3] + "', '" + event_data[4] + "'")
# Commit the changes to the database
connection.commit()
# Close the cursor and connection
bookings_db.close()
