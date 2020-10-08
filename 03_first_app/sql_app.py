import mysql.connector

# Establishing the connection object
con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

word=input("Enter the word: ")

# Here is the SQL Statement
query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)

# Storing the results
results = cursor.fetchall()

if results:
    for result in results:
        print(result[0])
else:
    print("No word found!")