import csv
import datetime

def create(h, m, s):
    if 0<=h<24 and 0<=m<60 and 0<=s<60:
        return {
            "h": h,
            "m": m,
            "s": s
        }
    return "Format incorrect"

def get_hour(time):
    return time["h"]

def get_min(time):
    return time["m"]

def get_sec(time):
    return time["s"]

def compare(time_1, time_2):
    time_1.split(';')
    time_2.split(';')
    diff = datetime.time(int(time_1[0]) , int(time_1[1]), int(time_1[2]))\
         - datetime.time(int(time_2[0]), int(time_2[1]), int(time_2[2]))
    
    return diff.total_seconds()

def to_string(time):
    return(f"{time['h']}h{time['m']}m{time['s']}s")