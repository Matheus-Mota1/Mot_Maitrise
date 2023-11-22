import mariadb
import sys

#Connect to MariaDB plataform
try:
	conn = mariadb.connect(
		user="folclore",
		password="Folclore",
		host="localhost",
		port=3306,
		database="library")
	
	#Get Cursor
	cur = conn.cursor()
	print("Connection sucessfull")
	
except mariadb.Error as e:
	print(f"Error connecting to MariaDB plataform: {e}")
	sys.exit(1)

# Auto-Commit enable by defaut
conn.autocommit = False
    
conn.close()