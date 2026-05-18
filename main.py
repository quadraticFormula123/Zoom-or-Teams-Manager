import webbrowser
from datetime import datetime
from datetime import date
import pandas as pandas #imports pandas as pandas so you can call it by its name (example, i call it as curry and i call it curry. etc)
import time


meetings = {} #defining the meetings dictionary
if (input("Do you want to add a meeting?") == "yes"):
    meetings["url"] = input("Enter the meeting URL: ")
    meetings["date"] = input("Enter the meeting date (YYYY-MM-DD): ")
    meetings["time"] = input("Enter the meeting time (HH:MM)")
    another_meeting = input("Do you want to add another meeting?")
    while (another_meeting == "yes"):
        meetings["url"] = input("Enter the meeting URL: ")
        meetings["date"] = input("Enter the meeting date (YYYY-MM-DD): ") 
        meetings["time"] = input("Enter the meeting time (HH:MM) in 24 hour form. eg 15:26")
        another_meeting = input("Do you want to add another meeting?")
else:
    print("No more meetings. ")

while (1 == 1):
    current_time = pandas.Timestamp.now().floor("1min") #Gets the time now than rounds down it to one minute removing the seconds etc. 
    current_time = current_time.strftime("%H:%M") #.strftime is string format time so we format it in the way we want, here just by hour
    # and minute
    current_date = date.today()
    print(f"'{current_time}' and '{meetings["time"]}'")
    print(f"'{current_date}' and '{meetings["date"]}'")
    if (current_date == meetings["date"]):
        print("Same date")
        if (current_time == meetings["time"]):
            print("Same time")
            webbrowser.open(meetings["url"])
            time.sleep(60)
    
    time.sleep(1)  #rests for a second so CPU dosen't overload

    




 
