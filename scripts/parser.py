import datetime

class Parser:
    file = None

    def __init__ (self, fileName):
        self.file = open(fileName, 'r')

    def getAll(self):
        dataList = []
        data = [line.rstrip() for line in self.file]
        data = data[3:]
        for record in data:
            recordList = record.split()
            for i in range(2, len(recordList)):
                if recordList[i] == "---":
                    recordList[i] = None
                elif recordList[i].replace('.','',1).isdigit():
                    recordList[i] = float(recordList[i])
            recordDT = datetime.datetime.strptime(recordList[0] + " " + recordList[1], '%d.%m.%y %H:%M')
            recordList = recordList[1:]
            recordList[0] = recordDT
            dataList.append(recordList)
        return dataList

    def getNewerThan(self, timestamp):
        data = self.getAll()
        filteredData = []
        if timestamp == None or timestamp == "":
            inputDT = datetime.datetime(1,1,1,0,0,0,0)
        else:
            inputDT = timestamp 
        for record in data:
            recordDT = record[0]
            if recordDT > inputDT:
                record[0] = recordDT.strftime("%Y-%m-%d %H:%M")
                filteredData.append(record)
        return filteredData
