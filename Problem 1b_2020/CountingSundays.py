from datetime import date
def CountingSundays():
    numSun=0
    for year in range(1901,2001):
        for month in range(1,13):
            check=date(year,month,1).isoweekday()
            if check==7:
                numSun+=1
    print("###########################################################")
    print("#                                                         #")
    print("#      We have ",numSun, " Sundays from 1901 to 2000 falling    #")
    print("#                                                         #")
    print("###########################################################")


CountingSundays()