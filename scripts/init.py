import sys
import database
import parser

db = database.Database()
db.createTable()
if len(sys.argv) > 1:
    par = parser.Parser(sys.argv[1])
    records = par.getAll()
    db.insertMany(records)
