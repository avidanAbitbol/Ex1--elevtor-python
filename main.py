import csv
from Elevators import Elevators
from building import Building
from Calls import load_csv_calls, Calls


# time for each call(according to elevator param)
def playTime(elv=Elevators, call=Calls):
    playTime = float(elv.open_time) + float(elv.close_time) + float(elv.start_time) + (
                abs(float(call.src_floor) - float(call.dst_floor)) / float(elv.speed)) + float(elv.stop_time) + float(
        elv.open_time) + float(elv.close_time)
    return playTime


# check if the elevator have no calls
def isEmpty(elev=Elevators):
    if len(elev.elevCalls) <= 0:
        return True


# remove from the list calls that are done by time.
def doneCall(myBuild=Building, call=Calls):
    for i in myBuild.elvators:
        if len(i.elevCalls) > 0:
            for busy in i.elevCalls:
                if busy < float(call.time):
                    i.elevCalls.pop(i.elevCalls.index(busy))


# sorting the free elevators to check the best time.
def sortEmpty(emptyElevs=Elevators, call=Calls):
    ElevId = -1
    min = 11111111111111
    for i in range(len(emptyElevs)):
        temp = playTime(emptyElevs[i], call)
        if temp < min:
            min = temp
            ElevId = i
    return ElevId


# function to allocate the best elevator to this call
def get_allocate(myBuild=Building, call=Calls):
    ElevId = -1
    min = 11111111111111
    # erase calls that done until this new one appeared
    doneCall(myBuild, call)

    for i in range(len(myBuild.elvators)):
        # if there's no calls, sort and return the best empty elev. for this call
        if isEmpty(myBuild.elvators[i]):
            time = playTime(myBuild.elvators[i], call)
            if time < min:
                min = time
                ElevId = i
        call.elev_id = ElevId
    else:
        temp = abs(myBuild.elvators[i].elevCalls[-1] - float(call.time))
        if temp < min:
            min = temp
            ElevId = i
        call.elv_id = ElevId
        # push new call to chosen elev. list
        myBuild.elvators[ElevId].elevCalls.append(playTime(myBuild.elvators[ElevId], call) + float(call.time))

        return ElevId


def output(file_build, file_calls, file_update_calls):
    myBuild = Building(0, 0)
    myBuild.load_json_build(file_build)
    list_calls = load_csv_calls(file_calls)
    newCalls = []
    for i in list_calls:
        get_allocate(myBuild, i)
        newCalls.append(i.__dict__.values())
    with open(file_update_calls, 'w', newline="") as f:
        csw = csv.writer(f)
        csw.writerows(newCalls)
    return file_update_calls


output("B3.json", "Calls_c.csv", "output.csv")

