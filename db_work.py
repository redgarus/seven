import sqlite3


db = sqlite3.connect("databaze.db")
sql = db.cursor()

sql.excute("""CREATE TABLE IF NOT EXISTS users(
	id INT PRIMARY KEY,
	title TEXT,
	txt TEXT,
	author TEXT
	)""")

db.commit()

sql.close()
db.close()