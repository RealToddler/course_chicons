# REFACTO : DONE, WORKING : TRUE, DOCSTRING : DONE, COMMENT : DONE
def create(h, m, s):
    """
    This function returns a dict created from the given time indications.
    create() admit three args:
    - h (type int) => hours part of the time.
    - m (type int) => minutes part of the time.
    - s (type int) => seconds part of the time.
    """
    if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
        return {
            'h': h,
            "min": m,
            "sec": s
        }
    return "Incorrect format"


# REFACTO : DONE, WORKING : TRUE, DOCSTRING : DONE, COMMENT : DONE
def get_hour(time):
    """
    This function returns the hours part of the time dict.
    get_hour() only admit one arg:
    - time (type dict) = > object returned by create() function
    """
    return time['h']


# REFACTO : DONE, WORKING : TRUE, DOCSTRING : DONE, COMMENT : DONE
def get_min(time):
    """
    This function returns the minutes part of the time dict.
    get_min() only admit one arg:
    - time (type dict) = > object returned by create() function
    """
    return time["min"]


# REFACTO : DONE, WORKING : TRUE, DOCSTRING : DONE, COMMENT : DONE
def get_sec(time):
    """
    This function returns the secondes part of the time dict.
    get_sec() only admit one arg:
    - time (type dict) = > object returned by create() function
    """
    return time["sec"]


# REFACTO : DONE, WORKING : TRUE, DOCSTRING : DONE, COMMENT : DONE
def compare(time1, time2):
    """
    This function returns the difference between two given times.
    compare() admit two args:
    - time1 (type dict) = > reference time
    - time2 (type dict) = > time to compare with
    """
    # converts time from time1 & time2 dicts to seconds 
    time1ToSec = time1['h'] * 3600 + time1["min"] * 60 + time1["sec"]
    time2ToSec = time2['h'] * 3600 + time2["min"] * 60 + time2["sec"]
    
    # difference in seconds between the two times 
    deltaSec = time1ToSec - time2ToSec
    
    sign = '-' if deltaSec < 0 else '+' # ternary

    # convert back the difference between the two times in hours, minutes, seconds format
    hours = abs(deltaSec) // (60*60)
    minutes = (abs(deltaSec) // (60*60)) // 60
    seconds  = (abs(deltaSec) // (60*60*60)) // 60
    return "%s %dh%dmn%ds" % (sign, hours, minutes, seconds) # variadic functions
    

# REFACTO : DONE, WORKING : TRUE, DOCSTRING : DONE, COMMENT : DONE
def to_string(time):
    """
    This function converts a time dict into a string format and returns it.
    to_string() only admit one arg:
    - time (type dict) = > object returned by create() function
    """
    return"%dh%dmn%ds" % (time['h'], time["min"], time["sec"])

