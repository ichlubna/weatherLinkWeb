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
                if not recordList[i].replace('.','',1).isdigit():
                    if not recordList[i] == "---":
                        recordList[i] = "\""+str(recordList[i])+"\""
            print(record)
            recordDT = datetime.datetime.strptime(recordList[0] + " " + recordList[1], '%d.%m.%y %H:%M')
            recordList = recordList[1:]
            recordList[0] = recordDT
            dataList.append(recordList)
        return dataList

    def getNewerThan(self, timestamp):
        data = self.getAll()
        filteredData = []
        inputDT = timestamp 
        for record in data:
            recordDT = record[0]
            if recordDT > inputDT:
                record[0] = recordDT.strftime("\"%Y-%m-%d %H:%M\"")
                filteredData.append(" ".join(record))
        return filteredData
