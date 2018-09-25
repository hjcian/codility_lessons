# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
class TimePoint(object):
    START = 0
    END = 1
    def __init__(self, string, enum):
        s = string.split(":")
        self.hour = int(s[0])
        self.min = int(s[1])
        self.enum = enum
    
    # @property
    # def show(self):
    #     return self.hour, self.min
        
    @property
    def type(self):
        return self.enum

    def __repr__(self):
        return "TimePoint({}, {}, {})".format(self.hour, self.min, "s" if self.type == TimePoint.START else "e")
    def __str__(self):
        return "({}, {}, {})".format(self.hour, self.min, "s" if self.type == TimePoint.START else "e")

    def __sub__(self, other):
        diff_hour = self.hour - other.hour
        diff_min = self.min - other.min
        if diff_min < 0:
            diff_min += 60
            diff_hour -= 1
        return diff_hour * 60 + diff_min

    # def __eq__(self, other):
    #         return (self.hour == other.hour) and (self.min == other.min)

def parsing(line):
    l = line.split(" ")
    time_interval = l[1].split("-")
    start_time = TimePoint(time_interval[0], TimePoint.START)
    end_time = TimePoint(time_interval[1], TimePoint.END)
    return l[0], start_time, end_time

def solution(S):
    # write your code in Python 3.6
    week_seq = { "Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6, }
    data = [[TimePoint("00:00", TimePoint.END)] for i in range(7)]
    for i in S.splitlines():
        Ddd, startpoint, endpoint = parsing(i)
        week_day_idx = week_seq.get(Ddd)
        data[week_day_idx].append(startpoint)
        data[week_day_idx].append(endpoint)
    
    max_sleep_min = 0
    posible_sleep_interval_list = []
    for key in week_seq:
        d = data[week_seq[key]]
        d.append(TimePoint("24:00", TimePoint.START))
        d.sort(key=lambda x: x.hour)
        posible_sleep_interval = [d[idx + 1] - d[idx] for idx in range(len(d) - 1) if d[idx + 1].type == TimePoint.START]
        # print(key)
        # print(d)
        # print(posible_sleep_interval)
        max_sleep_min = max(max(posible_sleep_interval), max_sleep_min)
        posible_sleep_interval_list.append(posible_sleep_interval)

    for idx in range(len(posible_sleep_interval_list) - 1):
        today_last = posible_sleep_interval_list[idx][-1]
        tomorrow_first = posible_sleep_interval_list[idx + 1][0]
        max_sleep_min = max(max_sleep_min, today_last + tomorrow_first)
    return max_sleep_min
    
    


S = "Sun 10:00-20:00\n\
Fri 05:00-10:00\n\
Fri 16:30-23:50\n\
Sat 10:00-24:00\n\
Sun 01:00-04:00\n\
Sat 02:00-06:00\n\
Tue 03:30-18:15\n\
Tue 19:00-20:00\n\
Wed 04:25-15:14\n\
Wed 15:14-22:40\n\
Thu 00:00-23:59\n\
Mon 05:00-13:00\n\
Mon 15:00-21:00"
print(solution(S))

S = "Mon 01:00-23:00\n\
Tue 01:00-23:00\n\
Wed 01:00-23:00\n\
Thu 01:00-23:00\n\
Fri 01:00-23:00\n\
Sat 01:00-23:00\n\
Sun 01:00-21:00"

print(solution(S))
