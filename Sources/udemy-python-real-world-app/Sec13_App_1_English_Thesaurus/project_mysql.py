# Using a database to store the dictionary, will improve the performance of the application.
# mysql-connector-python is a third-party library
# install it by pip install mysql-connector-python
import mysql.connector

# establish a connection
con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

# Create a cursor object to navigate through the database
cursor = con.cursor()

# Get the word from the user
word = input("Enter word: ")

# Do a query
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '&s" % word)

# Get the actual data
results = cursor.fetchall()

# print("DEBUG: type(result) = " + str(type(results)))

if results: # Check whether the results are empty
    for result in results:
        print(result[1])
else:
    print("No word found!")