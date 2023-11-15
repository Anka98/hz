
# Online Python - IDE, Editor, Compiler, Interpreter

import datetime as dt

FORMAT='%H:%M'

busy = [{'start':'10:30', 'stop':'10:50'},{'start':'18:40', 'stop':'18:50'},{'start':'14:40', 'stop':'15:50'},{'start':'16:40', 'stop':'17:20'},{'start':'20:05', 'stop':'20:20'}]
day_time_start = dt.datetime.strptime('9:00', FORMAT)
day_time_stop = dt.datetime.strptime('21:00', FORMAT)
free_time = []
busy_start = []
busy_stop = []
b = []
bb = []
#def pars_dict(dict_time_busy):
[(busy_start.append(i['start']),busy_stop.append(i['start'])) for i in busy]
#[busy_stop.append(i['start']) for i in busy]

        

busy_start.sort(key=lambda x: dt.datetime.strptime(x, FORMAT))
busy_stop.sort(key=lambda x: dt.datetime.strptime(x, FORMAT))
#    return busy_start, busy_stop

#def free_work_time(busy_start, busy_stop):
fulltimeday = ((day_time_stop.hour-day_time_start.hour)*60)//30
print(fulltimeday)
for times in range(fulltimeday):
    day_time_stop = day_time_start + dt.timedelta(minutes=30)
    free_time.append(day_time_start)
    for j in range(len(busy_start)):
        if day_time_start <= busy_start[j] and day_time_stop <= busy_start[j] and day_time_stop <= busy_stop[j]:
            b.append(day_time_start)
            bb.append(day_time_stop)
    day_time_start = day_time_start + dt.timedelta(minutes=30)    
print(f'{busy_start}')    
