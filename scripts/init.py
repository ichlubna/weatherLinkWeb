import sys
import database

db = database.Database()
#db.createTable()

if len(sys.argv) == 2:
    print(sys.argv[1])
