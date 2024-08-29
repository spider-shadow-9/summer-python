import datetime
import jdatetime
print("items\n1-say the time\n2-say the year\n3-say the month\n3-say the day\n4-say the date\n5-say the weekday\n6-show the time that I write\n")
while True:
    a=input("item:")
    if a=="1":
        s=input("show the weekday or not?")
        if s=="no":
            print(jdatetime.datetime.today())
        elif s=="yes":
            date=jdatetime.date.today()
            x=date.weekday
            b=""
            if x==6:
                print("jommeh",jdatetime.datetime.today())
            else:
                print(f"{date.weekday()}shanbeh",jdatetime.datetime.today())
    elif a=="2":
        date=jdatetime.date.today()
        print(date.year)
    elif a=="3":
        date=jdatetime.date.today()
        print(date.strftime('%b'))
    elif a=="4":
        print(jdatetime.date.today())
    elif a=="5":
        date=jdatetime.date.today()
        s=date.weekday()
        if s==6:
            print("jommeh")
        else:
            print(f"{s}shanbeh")
    elif a=="6":
        year=eval(input("enter the year:"))
        month=eval(input("enter the month:"))
        day=eval(input("enter the day:"))
        hour=eval(input("enter the hour:"))
        minute=eval(input("entr the minute:"))
        secound=eval(input("enter the scound:"))
        x=jdatetime.datetime(year,month,day,hour,minute,secound)
        print(x.strftime('%b'),x)