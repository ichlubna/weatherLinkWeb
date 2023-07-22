import time
import sys
import database
import parser

if len(sys.argv) == 1:
    print("Specify the weather data file that is being updated as the first argument!")
    exit(1)

pause = 5*60
while True:
    db = database.Database()
    last = db.getLastTimestamp()
    par = parser.Parser(sys.argv[1])
    newRecords = par.getNewerThan(last)
    newRecords.reverse()
    for record in newRecords:
        db.insert(record)
    db.close()
    time.sleep(pause)
