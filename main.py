
from Calls import *
from Elevators import Elevators
from Building import Building
from Calls import load_csv_calls


def playTime(elv=Elevators, call=Calls): #time for each call(acording to elevator param.
    speed = float(elv.speed)
    open = float(elv.open_time)
    close = float(elv.close_time)
    start = float(elv.start_time)
    stop = float(elv.stop_time)
    src = int(call.src_floor)
    dst = int(call.dst_floor)
    playTime = open+close+start+(abs(src - dst) / speed)+stop+open+close
    return playTime


def isEmpty(elev=Elevators):#check if the elev. have no calls
     if len(elev.elevCalls) <= 0:
            return True

def doneCall(myBuild=Building, call=Calls):
    for i in myBuild.elvators:
        if len(i.elevCalls) > 0:
            for busy in i.elevCalls:
                if busy < float(call.time):
                    i.elevCalls.pop(i.elevCalls.index(busy))

def sortEmpty(emptyElevs=Elevators,call=Calls):
    ElevId=-1
    min = 11111111111111
    for i in range (len(emptyElevs)):
          temp = playTime(emptyElevs[i], call)
          if temp < min:
            min = temp
            ElevId = i
    return ElevId

def allocate(myBuild=Building, call=Calls):
    ElevId = -1
    min = 11111111111111
    doneCall(myBuild, call)#erase calls that done until this new one appeared

    for i in range(len(myBuild.elvators)):

        if isEmpty(myBuild.elvators[i]):  #if there's no calls, sort and return the best enpty elev. for this call
            emptyElevs = []
            emptyElevs.append(myBuild.elvators[i])

        else:
            for i in range(len(myBuild.elvators)):
              temp = abs(myBuild.elvators[i].elevCalls[-1] - float(call.time))
              if temp < min:
                min = temp
                ElevId = i
            call.elv_id = ElevId
            myBuild.elvators[ElevId].elevCalls.append(playTime(myBuild.elvators[ElevId], call) + float(call.time))#push new call to choosen elev. list


            if len(emptyElevs)>0:
                ElevId = sortEmpty()
                myBuild.elvators[ElevId].elevCalls.append(playTime(myBuild.elvators[ElevId], call) + float(call.time))
                call.elev_id = ElevId
                return ElevId
            else:
                return ElevId



def output(file_build, file_calls, file_update_calls):
    myBuild = Building(0, 0)
    myBuild.load_json_build(file_build)
    list_calls = load_csv_calls(file_calls)
    newCalls = []
    for i in list_calls:
        allocate(myBuild, i)
        newCalls.append(i.__dict__.values())
    with open(file_update_calls, 'w', newline="") as f:
        csw = csv.writer(f)
        csw.writerows(newCalls)
    return file_update_calls

output("B5.json", "Calls_d.csv", "output.csv")
