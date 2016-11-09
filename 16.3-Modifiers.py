class Time:
    def __init__(self):
        self.minute = None
        self.second = None
        self.hour = None
    """Represents the time of day
    attributes: hour, minute, second
    """


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def increment(time, inc):
    time += inc
    return time


time = Time()
time.hour = 12
time.minute = 00
time.second = 00

print ('\nThe time to be incremented is ' + '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))


time.seconds = time_to_int(time)

inc_sec = raw_input('\nEnter the number of seconds to increment the time object by: ')

print ('\nThe amount time will be incremented by is: ' + str(inc_sec) + ' seconds.')


inc_seconds = increment(time.seconds, int(inc_sec))


time = int_to_time(inc_seconds)


if time.hour > 12:
    time.hour -= 12

print ('\nThe incremented time is ' + '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))
