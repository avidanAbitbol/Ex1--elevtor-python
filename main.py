from Building import *
from Elevator import *
from Calls import *

def playTime(elv=Elevator, call=Calls):
    playTime = float(elv.open_time) + float(elv.close_time) + float(elv.start_time) + (
                abs(float(call.src_floor) - float(call.dst_floor)) / float(elv.speed)) + float(elv.stop_time) + float(
        elv.open_time) + float(elv.close_time)
    return playTime

def emptySort(building=Building, call=Calls):#sort all empty elevators
    elev = building.elvators
    elevId = -1
    min = 999999999999
    for i in range(len(elev)):
        if len(elev[i].elevCalls) <= 0:
            time = playTime(elev[i], call)
            if time < min:
                min = time
                elevId = i
    return elevId

def doneCall(bui=Building, call=Calls):
    for i in bui.elvators:
        if len(i.elevCalls) > 0:
            for j in i.elevCalls:
                if j < float(call.time):
                    i.elevCalls.pop(i.elevCalls.index(j))

def getAlocate(build=Building, call=Calls):
    Elevs = len(build.elvators)
    ElevId = -1
    min = 99999999
    doneCall(build, call)#erase "done calls"(calls that done before current call time) from all elevators.
    emptyBest = emptySort(build, call)
    if emptyBest != -1:  #if empty elevatrors exist, check the better one
        call.elv_id = emptyBest
        build.elvators[emptyBest].elevCalls.append(playTime(build.elvators[emptyBest], call) + float(call.time) + 0)
        return emptyBest

    else:
        for i in range(Elevs):#if there is no empty, looks for the better one (best time between finish last to new one)
            time = abs(build.elvators[i].elevCalls[-1] - float(call.time) + playTime(build.elvators[i], call))
            if time < min:
                min = time
                ElevId = i
        call.elv_id = ElevId
        build.elvators[ElevId].elevCalls.append(playTime(build.elvators[ElevId], call) + float(call.time) + min)
    return ElevId

def output(file_build, file_calls, file_update_calls):
    MyBuilding = Building(0, 0)
    MyBuilding.BuildFromJason(file_build)
    list_calls = CallsFromCsv(file_calls)
    CallsList = []
    for call in list_calls:
        getAlocate(MyBuilding, call)
        CallsList.append(call.__dict__.values())
    with open(file_update_calls, 'w', newline="") as f:
        csw = csv.writer(f)
        csw.writerows(CallsList)
    return file_update_calls


output("B3.json", "Calls_a.csv", "output.csv")
