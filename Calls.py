import csv





class Calls:
    def __init__(self, call_num, time, src_floor, dst_floor, state, elv_id):
        self.call_num = call_num
        self.time = time
        self.src_floor = src_floor
        self.dst_floor = dst_floor
        self.state = state
        self.elv_id = elv_id

    def __repr__(self) -> str:
        return f"repr call_num:{self.call_num} time:{self.time} src_floor:{self.src_floor} " \
               f"dst_floor:{self.dst_floor} elv_id:{self.elv_id} "

def CallsFromCsv(file):
        calls_list = []
        with open(file) as f:
            calls_data = csv.reader(f)
            for row in calls_data:
                call = Calls(call_num=row[0], time=float(row[1]), src_floor=int(row[2]), dst_floor=int(row[3]),
                             state=row[4], elv_id=row[5])
                calls_list.append(call)
        return calls_list
