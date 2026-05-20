import webbrowser
from datetime import datetime
import time as time
from tkinter import * #imports all avaliable stuff in tkinter

window = Tk() #place window on computer screen, listens for events
window.geometry("520x520")#changes window size
window.title("Meetings Manager") #setting the window title
softwareIcon = PhotoImage(file='softwareIcon.png') #turning our png image into a photoImage and storing in softwareIcon
window.iconphoto(True, softwareIcon) #giving our window softwareIcon as its iconphoto
titleLabel = Label(window,text="Meetings Manager", font=('Arial',40,'bold'), fg='blue')
#titleLabel.pack() - actually packs our label into the window
titleLabel.place(x=5, y=5) #packs it but we can pace it in a specific place 
window.mainloop() #displays our window

#label - an area widget that holds a text and/or an image within a window

another_meeting = input("Do you want to add a/anotfher meeting?")

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