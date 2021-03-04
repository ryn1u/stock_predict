from datetime import timedelta, date

#counts to nearesst workday from starting day
#if starting day is not specified starts from today
#if delta is negative counts by previous days from start, else opposite
def get_workday(delta, starting_day = date.today()):
    one_day = timedelta(1)
    weekend = timedelta(2)

    delta_counter = abs(delta)
    count_backwards = True if delta < 0 else False

    while delta_counter > 0:
        starting_day = starting_day - one_day if count_backwards else starting_day + one_day
        if starting_day.isoweekday() == 7:
            starting_day = starting_day - weekend if count_backwards else starting_day + oneday
        elif starting_day.isoweekday() == 6:
            starting_day = starting_day - one_day if count_backwards else starting_day + weekend
        delta_counter -= 1
    
    return starting_day

#get date staring from starting_day counted from delta
#if starting day is not specified starts from today
#if delta is negative counts by previous days from start, else opposite
def get_day(delta, starting_day=date.today()):
    return starting_day + timedelta(delta)