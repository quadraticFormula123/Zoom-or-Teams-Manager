// Selectors for the add button and the popup container
const addNewMeetingButton = document.querySelector(".addNewMeeting")
const newMeetingInfoDiv = document.querySelector(".newMeetingInfoBox")

// Wire up the button to open the popup
addNewMeetingButton.addEventListener("click", addNewMeeting)

// Basic styles for the popup container (applied via JS so markup stays minimal)
newMeetingInfoDiv.style.padding = "18px"
newMeetingInfoDiv.style.boxSizing = "border-box"
newMeetingInfoDiv.style.display = "none" // hidden by default
newMeetingInfoDiv.style.position = "fixed"
newMeetingInfoDiv.style.zIndex = 9999

// Build popup contents: header, inputs (name, url, date, time) and a close button
function createPopupContents() {
    // Clear any existing children from previous opens
    newMeetingInfoDiv.innerHTML = ""

    // Close button (top-right)
    const closeBtn = document.createElement("button")
    closeBtn.textContent = "×"
    closeBtn.style.position = "absolute"
    closeBtn.style.right = "12px"
    closeBtn.style.top = "8px"
    closeBtn.style.background = "transparent"
    closeBtn.style.border = "none"
    closeBtn.style.fontSize = "24px"
    closeBtn.style.cursor = "pointer"
    closeBtn.addEventListener("click", () => {
        newMeetingInfoDiv.style.display = "none"
    })

    // Title for the popup
    const header2 = document.createElement("h3")
    header2.textContent = "New Meeting Info"

    // Meeting name field
    const meetingNameTag = document.createElement("p")
    meetingNameTag.textContent = "New Meeting Name"
    const meetingName = document.createElement("input")
    meetingName.placeholder = "Meeting name . . . "
    meetingName.style.borderRadius = "4px"
    meetingName.style.border = "1px solid #ccc"
    meetingName.style.padding = "8px"
    meetingName.style.width = "100%"

    // Meeting URL field
    const urlTag = document.createElement("p")
    urlTag.textContent = "Meeting URL"
    const urlInput = document.createElement("input")
    urlInput.placeholder = "https://..."
    urlInput.style.borderRadius = "4px"
    urlInput.style.border = "1px solid #ccc"
    urlInput.style.padding = "8px"
    urlInput.style.width = "100%"

    // Date field (YYYY/MM/DD) - text input for manual date format entry
    const dateTag = document.createElement("p")
    dateTag.textContent = "Meeting Date (YYYY/MM/DD - with leading zeros if necessary)"
    const dateInput = document.createElement("input")
    dateInput.type = "text"
    dateInput.placeholder = "2026/05/21"
    dateInput.style.borderRadius = "4px"
    dateInput.style.border = "1px solid #ccc"
    dateInput.style.padding = "8px"
    dateInput.style.width = "100%"

    // Time field (24-hour, e.g., 15:16) - using type=time enforces 24-hour input in most browsers
    const timeTag = document.createElement("p")
    timeTag.textContent = "Meeting Time (24-hour HH:MM)"
    const timeInput = document.createElement("input")
    timeInput.type = "time"
    timeInput.style.borderRadius = "4px"
    timeInput.style.border = "1px solid #ccc"
    timeInput.style.padding = "8px"
    timeInput.style.width = "100%"

    // Append elements to the popup container
    newMeetingInfoDiv.appendChild(closeBtn)
    newMeetingInfoDiv.appendChild(header2)
    newMeetingInfoDiv.appendChild(meetingNameTag)
    newMeetingInfoDiv.appendChild(meetingName)
    newMeetingInfoDiv.appendChild(document.createElement("br"))
    newMeetingInfoDiv.appendChild(urlTag)
    newMeetingInfoDiv.appendChild(urlInput)
    newMeetingInfoDiv.appendChild(document.createElement("br"))
    newMeetingInfoDiv.appendChild(dateTag)
    newMeetingInfoDiv.appendChild(dateInput)
    newMeetingInfoDiv.appendChild(document.createElement("br"))
    newMeetingInfoDiv.appendChild(timeTag)
    newMeetingInfoDiv.appendChild(timeInput)

    // Basic popup sizing and look
    newMeetingInfoDiv.style.backgroundColor = "#f7f7f7"
    newMeetingInfoDiv.style.width = "420px"
    newMeetingInfoDiv.style.maxWidth = "92%"
    newMeetingInfoDiv.style.height = "auto"
    newMeetingInfoDiv.style.borderRadius = "12px"
    newMeetingInfoDiv.style.top = "50%"
    newMeetingInfoDiv.style.left = "50%"
    newMeetingInfoDiv.style.transform = "translate(-50%, -50%)"
    newMeetingInfoDiv.style.boxShadow = "0 10px 40px rgba(0,0,0,0.15)"
}

// Show the popup (if not already visible)
function addNewMeeting() {
    // If popup already visible, do nothing
    if (newMeetingInfoDiv.style.display === "block")  {
        return
    }

    createPopupContents()
    // display: block makes the popup visible (changes from hidden display: none state)
    newMeetingInfoDiv.style.display = "block"
}
