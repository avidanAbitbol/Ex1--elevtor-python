
class Elevator:
    def __init__(self, id, speed, min_floor, max_floor, close_time, open_time, start_time, stop_time, elevCalls):
        self.id = id
        self.speed = speed
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.close_time = close_time
        self.open_time = open_time
        self.start_time = start_time
        self.stop_time = stop_time
        self.elevCalls = elevCalls

    def __repr__(self) -> str:
        return f"repr _id:{self.id} speed:{self.speed} min_floor:{self.min_floor} " \
               f"max_floor:{self.max_floor} close_time:{self.close_time} " \
               f"open_time:{self.open_time} start_time:{self.stop_time} stop_time:{self.stop_time} time_busy:{self.elevCalls}" \
