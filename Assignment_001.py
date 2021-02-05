def is_leap(year):
    leap = False
    if year in range(1900,100000):
        if (year % 4) == 0:
            if (year % 400) == 0:
                if (year % 100) == 0:
                    leap = False
                else:
                     leap = True
    else:
        leap = False
    return leap

year = int(raw_input())
