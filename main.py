import webbrowser
from datetime import datetime
import time as time
from tkinter import * # imports all available names from tkinter (not used in this script)

# Simple CLI collection of meetings and a loop to open meeting URLs at the scheduled time.
another_meeting = input("Do you want to add a/anotfher meeting?")

meetings = []
while (another_meeting.lower() == "yes"):

    # Ask user for meeting details. Date should be YYYY-MM-DD, time in 24-hour HH:MM.
    url = input("Enter the meeting URL: ")
    dateOfMeeting = input("Enter the meeting date (in this form: YYYY-MM-DD) ...  ") 
    timeOfMeeting = input("Enter the meeting time (HH:MM) in 24 hour form. eg 15:26 ... ")
    
    # Store meeting as a simple dictionary
    meeting = {
        "url": url,
        "dateOfMeeting": dateOfMeeting, 
        "timeOfMeeting": timeOfMeeting
    }

    meetings.append(meeting)

    # Prompt to add another meeting
    another_meeting = input("Do you want to add another meeting?")

else:
    # When user is done adding meetings
    print("Ok. No more meetings.")

# Infinite loop that checks the current date/time and opens matching meeting URLs.
while (1==1):
    currentTime = datetime.now().strftime("%H:%M")
    currentDate = datetime.now().strftime("%Y-%m-%d")
    for meeting in meetings:
        # Compare stored date and time strings to current date/time
        if(currentDate == meeting["dateOfMeeting"]):
                print("Dates same.")
                if(currentTime == meeting["timeOfMeeting"]):
                    print("Same time. ")
                    webbrowser.open_new_tab(meeting["url"])
                    # Wait a minute after opening to avoid opening repeatedly for the same minute
                    time.sleep(60)
    # Small sleep to avoid busy-waiting
    time.sleep(1)