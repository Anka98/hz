
# Online Python - IDE, Editor, Compiler, Interpreter

import datetime as dt

FORMAT='%H:%M'
day_start = '9:00'
day_stop = '21:00'
busy = [{'start':'10:30', 'stop':'10:50'},{'start':'18:40', 'stop':'18:50'},{'start':'14:40', 'stop':'15:50'},{'start':'16:40', 'stop':'17:20'},{'start':'20:05', 'stop':'20:20'}]
busy_start, busy_stop = [],[]
 
busy_work_start, busy_work_stop  = [],[]


def pars_dict(start, stop, dict_busy):
    day_time_start = dt.datetime.strptime(day_start, FORMAT)
    day_time_stop = dt.datetime.strptime(day_stop, FORMAT)
    [(busy_start.append(i['start']),busy_stop.append(i['stop'])) for i in busy]
    busy_start.sort()
    busy_stop.sort()
    return busy_start, busy_stop, day_time_start, day_time_stop

def free_work_time(day_time_stop,day_time_start,busy_start, busy_stop):

    fulltimeday = ((day_time_stop.hour-day_time_start.hour)*60)//30
    
    for times in range(fulltimeday):
        flug = True 
        day_time_stop = day_time_start + dt.timedelta(minutes=30)
        for j in range(len(busy_start)):
            
            if (day_time_start <= dt.datetime.strptime(busy_start[j], FORMAT) and day_time_stop <= dt.datetime.strptime(busy_start[j], FORMAT) and day_time_stop <= dt.datetime.strptime(busy_stop[j], FORMAT)) or (day_time_start > dt.datetime.strptime(busy_start[j], FORMAT) and day_time_stop > dt.datetime.strptime(busy_stop[j], FORMAT)):
                prom_start = day_time_start
            else:
                prom_start_1 = dt.datetime.strptime(busy_stop[j], FORMAT)
                #print(prom_start_1)
                flug = False
        
        if day_time_start>= dt.datetime.strptime('20:30', FORMAT):
            break
        
        if flug == True:
            busy_work_start.append(prom_start)
            
            busy_work_stop.append(prom_start + dt.timedelta(minutes=30))
        else:
            busy_work_start.append(prom_start_1)
            prom_start = prom_start_1 
            busy_work_stop.append(prom_start_1 + dt.timedelta(minutes=30))
            
        day_time_start = prom_start + dt.timedelta(minutes=30)
        #print(day_time_start)
           
print(free_work_time(pars_dict(day_start, day_stop, busy)))



#print(fullday.get('start'))
