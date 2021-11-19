import json
from Elevator import Elevator


class Building(object):
    elvators = [Elevator]

    def __init__(self, min_floor, max_floor, elvators=[Elevator]):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.elvators = elvators

    def BuildFromJason(self, file):
        elevators = []
        with open(file, "r") as f:
            B = json.load(fp=f)
            self.min_floor = B["_minFloor"]
            self.max_floor = B["_maxFloor"]
            for elev in B["_elevators"]:
                el = Elevator(id=elev["_id"], speed=elev["_speed"], min_floor=elev["_minFloor"],max_floor=elev["_maxFloor"], close_time=elev["_closeTime"], open_time=elev["_openTime"],start_time=elev["_startTime"],stop_time=elev["_stopTime"], elevCalls=[])
                elevators.append(el)
            self.elvators = elevators

        return self
