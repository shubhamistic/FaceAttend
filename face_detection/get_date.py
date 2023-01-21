from datetime import date , datetime


def get_date():
    now = datetime.now()

    day = now.strftime("%d")
    mon = now.strftime("%m")

    if mon == '01':
        mon = 'JAN'
    elif mon == '02':
        mon = 'FEB'
    elif mon == '03':
        mon = 'MAR'
    elif mon == '04':
        mon = 'APR'
    elif mon == '05':
        mon = 'MAY'
    elif mon == '06':
        mon = 'JUN'
    elif mon == '07':
        mon = 'JUL'
    elif mon == '08':
        mon = 'AUG'
    elif mon == '09':
        mon = 'SEP'
    elif mon == '10':
        mon = 'OCT'
    elif mon == '11':
        mon = 'NOV'
    elif mon == '12':
        mon = 'DEC'

    year = now.strftime("%Y")[2:]

    sec = now.strftime("%S")
    min_ = now.strftime("%M")
    hour = now.strftime("%H")

    return day, mon, year, sec, min_, hour
