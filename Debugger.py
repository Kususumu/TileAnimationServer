#Debug function use to show list
import time

# Use to show a list With Information Help
def showList(list,informa):
    for i in range(len(list)):
        print(i,informa,list[i])


# Use to stop the system time
def stopTime(time):
    print("Start : %s" % time.ctime())
    time.sleep(time)
    print("End : %s" % time.ctime())