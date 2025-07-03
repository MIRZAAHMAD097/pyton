#lesson 15
#1
import sqlite3

conn = sqlite3.connect('my_database')
cursor = conn.cursor()

#2
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster(
Name TEXT,
Species TEXT,
Age INTEGER)
""")

cursor.execute("DELETE FROM Roster")

data = [
    ("Benjamin Franklin", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

cursor.executemany("INSERT INTO Roster(Name, Species, Age) VALUES(?,?,?)", data)

#3
cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")

#4
print("\nBajoran crew members: ")
cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
results = cursor.fetchall()

for name, age in results:
    print(f"Name: {name}, Age: {age}")

conn.commit()
conn.close()
