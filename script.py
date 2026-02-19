import pyautogui
import time
import obsws_python as obs
import subprocess


Meeting_id = 'your_meeting_id'
Meeting_Passkey = 'your_meeting_passkey'

# Before using change "screens" folder path to your own
def join_meeting_zoom_OS_Lecture():
    subprocess.Popen("C:/Users/Kvova/AppData/Roaming/Zoom/bin/Zoom.exe")
    print("Waiting for Zoom to open...")
    time.sleep(15)
    location = pyautogui.locateOnScreen("D:/ZoomRecorder/screens/Join1.png")
    pyautogui.click(location)
    pyautogui.typewrite(Meeting_id)
    location = pyautogui.locateOnScreen("D:/ZoomRecorder/screens/ID_Join.png")
    pyautogui.click(location)
    pyautogui.typewrite(Meeting_Passkey)
    location = pyautogui.locateOnScreen("D:/ZoomRecorder/screens/Join_meeting.png")
    pyautogui.click(location)
    location = pyautogui.locateOnScreen("D:/ZoomRecorder/screens/MuteIcon.png")
    pyautogui.click(location)
    location = pyautogui.locateOnScreen("D:/ZoomRecorder/screens/JoinFinal.png")
    pyautogui.click(location)




def record(): # Wont work if your OBS is not open and your not connected to the WebSocket
    client = obs.ReqClient(host = 'localhost', port = 4455, password = 'Enter ur password')
    client.start_record()
    time.sleep(5400) # How long to record in secs 
    client.stop_record()

join_meeting_zoom_OS_Lecture()
record()

