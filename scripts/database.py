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

    def createTable(self):
        command = "CREATE TABLE "+self.table.name+"("+self.table.header+");"
        if self.debug == True:
            print(command)
        self.database.cursor().execute(command)

    def insert(self, record):
        values = record.split()
        valuesString = ','.join(values)
        valuesString = valuesString.replace(",", " ", 1)
        valuesString = valuesString.replace("---", "NULL")
        command = "INSERT INTO "+self.table.name+" VALUES ("+valuesString+");"
        if self.debug == True:
            print(command)
        self.database.cursor().execute(command)
    
    def getLastTimestamp(self):
        command = "SELECT DateTime FROM "+self.table.name+" ORDER BY DateTime DESC LIMIT 1"
        command = "SELECT * FROM `WeatherHistory` WHERE 1"
        cursor = self.database.cursor(buffered=True)
        cursor.execute(command)
        return cursor.fetchall()[0][0]

