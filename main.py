import webbrowser
from datetime import datetime
import time as time

another_meeting = input("Do you want to add a/another meeting?")

meetings = []
while (another_meeting.lower() == "yes"):

    url = input("Enter the meeting URL: ")
    dateOfMeeting = input("Enter the meeting date (in this form: YYYY-MM-DD) ...  ") 
    timeOfMeeting = input("Enter the meeting time (HH:MM) in 24 hour form. eg 15:26 ... ")
    
    meeting = {
        "url": url,
        "dateOfMeeting": dateOfMeeting, 
        "timeOfMeeting": timeOfMeeting
    }

    meetings.append(meeting)

    another_meeting = input("Do you want to add another meeting?")

else:
    print("Ok. No more meetings.")

while (1==1):
    currentTime = datetime.now().strftime("%H:%M")
    currentDate = datetime.now().strftime("%Y-%m-%d")
    for meeting in meetings:
        if(currentDate == meeting["dateOfMeeting"]):
                print("Dates same.")
                if(currentTime == meeting["timeOfMeeting"]):
                    print("Same time. ")
                    webbrowser.open_new_tab(meeting["url"])
                    time.sleep(60)
    time.sleep(1)
    
        