import threading

digitList = [1,2,3,4,5,6,7,8,9,0]
dozensList = [10,20,30,40,50,60,70,80,90,100]

class RunnerDozens(threading.Thread):
    def run(self):
        for d in dozensList:
            print("I am thread {} from dozensList. Next value is {}".format(self.getName(),d))

class RunnerDigits(threading.Thread):
    def run(self):
        for dig in digitList:
            print("I am thread {} from digitList. Next value is {}".format(self.getName(),dig))
	

digitThread = RunnerDigits()
dozensThread = RunnerDozens()

digitThread.start()
dozensThread.start()