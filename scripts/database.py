import mysql.connector
import credentials

class Database:
    database = None
    debug = True

    class Table:
        name = "WeatherHistory"
        header = ("DateTime DATETIME,"
                           "TempOut FLOAT,"
                           "HiTemp FLOAT,"
                           "LowTemp FLOAT,"
                           "OutHum FLOAT,"
                           "DewPt FLOAT,"
                           "WindSpeed FLOAT,"
                           "WindDir VARCHAR(10),"
                           "WindRun FLOAT,"
                           "HiSpeed FLOAT,"
                           "HiDir VARCHAR(10),"
                           "WindChill FLOAT,"
                           "HeatIndex FLOAT,"
                           "THWIndex FLOAT,"
                           "THSWIndex FLOAT,"
                           "Bar FLOAT,"
                           "Rain FLOAT,"
                           "RainRate FLOAT,"
                           "SolarRad FLOAT,"
                           "SolarEnergy FLOAT,"
                           "HiSolarRad FLOAT,"
                           "UVIndex FLOAT,"
                           "UVDose FLOAT,"
                           "HiUV FLOAT,"
                           "HeatDD FLOAT,"
                           "CoolDD FLOAT,"
                           "InTemp FLOAT,"
                           "InHum FLOAT,"
                           "InDev FLOAT,"
                           "InHeat FLOAT,"
                           "InEMC FLOAT,"
                           "InAirDensity FLOAT,"
                           "Temp2nd FLOAT,"
                           "Hum2nd FLOAT,"
                           "ET FLOAT,"
                           "Soil1Moist FLOAT,"
                           "SoilTemp1 FLOAT,"
                           "WindSamp FLOAT,"
                           "WindTx FLOAT,"
                           "ISSRecept FLOAT,"
                           "ArcInt FLOAT"
                )

    table = Table()
    credentials = credentials.Credentials()

    def __init__(self):
        self.database = mysql.connector.connect(
            host = self.credentials.host,
            port = self.credentials.port,
            user = self.credentials.userName,
            password = self.credentials.password,
            database = self.credentials.database)

    def executeCommand(self, command):
        if self.debug == True:
            print(command) 
        cursor = self.database.cursor()#(buffered=True)
        cursor.execute(command)
        result = cursor.fetchone()
        resultString = ""
        if result != None:
            resultString = result[0]
        if self.debug == True:
            print(resultString)
        return resultString

    def createTable(self):
        self.executeCommand("CREATE TABLE "+self.table.name+"("+self.table.header+", PRIMARY KEY(DateTime));")

    def insert(self, record):
        record = ["\""+str(v)+"\"" if type(v) == str else v for v in record]
        record = ['NULL' if v is None else v for v in record]
        valuesString = ','.join([str(i) for i in record])
        self.executeCommand("INSERT INTO "+self.table.name+" VALUES ("+valuesString+");")
        self.database.commit()
    
    def insertMany(self, records):
        valuesString = ("%s, "*len(records[0]))[:-2]
        cursor = self.database.cursor()
        cursor.executemany("INSERT INTO "+self.table.name+" VALUES ("+valuesString+");", [tuple(x) for x in records])
        self.database.commit()
    
    def getLastTimestamp(self):
        command = "SELECT DateTime FROM "+self.table.name+" ORDER BY DateTime DESC LIMIT 1"
        return self.executeCommand(command)

