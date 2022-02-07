def solution(a, b):
    import datetime  
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return days[datetime.datetime(2016, a, b).weekday()]