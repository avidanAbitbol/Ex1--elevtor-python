import csv
from Elevators import Elevators
from Building import Building
from Calls import Calls, loadCalls


# time for each call(according to elevator param)
def playTime(elv=Elevators, call=Calls):
    time = float(elv.open_time) + float(elv.close_time) + float(elv.start_time) + (
            abs(float(call.src_floor) - float(call.dst_floor)) / float(elv.speed)) \
               + float(elv.stop_time) + float(elv.open_time) + float(elv.close_time)
    return time


# remove from the list calls that are done by time.
def doneCall(myBuild=Building, call=Calls):
    for i in myBuild.elvators:
        if len(i.elevCalls) > 0:
            for j in i.elevCalls:
                if j < float(call.time):
                    i.elevCalls.pop(i.elevCalls.index(j))


# function to allocate the best elevator to this call
def get_allocate(myBuild=Building, call=Calls):
    bestFree = -1
    bestBusy = -1
    minFree = 11111111111111
    minBusy = 11111111111111
    doneCall(myBuild, call)  # erase calls that done until this new one appeared

    for i in range(len(myBuild.elvators)):  # passes over all elevators in this building
        if len(myBuild.elvators[i].elevCalls) <= 0:  # means that this elevator don't have calls
            time = playTime(myBuild.elvators[i], call)
            if (time <= minFree):
                minFree = time
                bestFree = i
        else:  #
            time = abs(myBuild.elvators[i].elevCalls[-1] - float(call.time))
            if (time <= minBusy):
                minBusy = time
                bestBusy = i

    if (bestFree != -1):
        myBuild.elvators[bestFree].elevCalls.append(playTime(myBuild.elvators[bestFree], call) + float(call.time))
        return bestFree
    else:
        myBuild.elvators[bestBusy].elevCalls.append(playTime(myBuild.elvators[bestBusy], call) + float(call.time))
        return bestBusy


def output(file_build, file_calls, file_update_calls):
    b = Building(0, 0)
    b.load_json_build(file_build)
    list_calls = loadCalls(file_calls)
    newCalls = []
    for i in list_calls:
        get_allocate(b, i)
        newCalls.append(i.__dict__.values())
    with open(file_update_calls, 'w', newline="") as f:
        csw = csv.writer(f)
        csw.writerows(newCalls)
    return file_update_calls


output("B1.json", "Calls_d.csv", "output.csv")

