import sqlite3

db = sqlite3.connect("database.db")
cursor = db.cursor()

cursor.execute("DELETE FROM desechos")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='desechos'")

db.commit()
db.close()

print("Contador reiniciado")
