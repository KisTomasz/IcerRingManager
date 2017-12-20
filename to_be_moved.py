# board manager
from wx import ListCtrl
import time
from datetime import datetime
from datetime import timedelta


def updateTimesOnParticipantList(listCtrl):
    itemCount = listCtrl.GetItemCount()
    index = 0
    for item in range(0, itemCount, 1):
        entryTimeStr = listCtrl.GetItem(index, 3).GetText()
        entryTimeDate = datetime.strptime(entryTimeStr, '%H:%M:%S')
        print entryTimeDate
        boughtHoursStr = listCtrl.GetItem(index, 4).GetText()
        currentDate = datetime.strptime(time.strftime("%H:%M:%S"), '%H:%M:%S')
        print currentDate
        timeDiff = entryTimeDate + timedelta(hours=int(boughtHoursStr)) - currentDate
        print str(timeDiff)
        listCtrl.SetStringItem(index, 5, str(timeDiff))
        index += 1


# ______________________________________________________________________________________________________________________
# obsluga timerow

def getCurrentTime():
    # return time.localtime(time.time())
    return time.strftime("%H:%M:%S")
