# Assignment 10

# Contact Tracing App
#	- Create a python program that will read QRCode using your webcam
#	- You may use any online QRCode generator to create QRCode
#	- All personal data are in QRCode 
#	- You may decide which personal data to include
#	- All data read from QRCode should be stored in a text file including the date and time it was read

# Note: 
#	- Search how to generate QRCode
#	- Search how to read QRCode using webcam
#	- Search how to create and write to text file
#	- Your source code should be in github before Feb 19
#	- Create a demo of your program (1-2 min) and send it directly to my messenger.

# Supplemented pyzbar on the program for the apparent decoding of the data inside the Details Variable.
# Datetime Import for Updated Time Registry.
from pyzbar import pyzbar; from datetime import *; import time
# CV2 as the program interface for Live Webcam on User Default.
import cv2
"""
DEF FUNCTION FOR THE CALENDAR OF UPDATED REGISTRY - TO BE IMPORTED ON THE CONTACT TRACING INFORMATION TEXT FILE
"""
def record_scan(icon):
    BCHScan = pyzbar.decode(icon)
    for info in BCHScan:
        a, b, c, d = info.rect                                                                  # Settling up global parameters for the Font Layout on the Live Webcam.
        TxtBCHFile = info.data.decode('utf-8')                                                  # ASCII Standard Unicode Character
        cv2.rectangle(icon, (a, b),(a+c, b+d), (0, 0, 150), 3)                                  # ASCII Font Density
        cv2.rectangle(icon, (a, b),(a+c, b+d), (0, 150, 0), 3)                                  # ASCII Font Density
        TxtFont = cv2.FONT_HERSHEY_COMPLEX_SMALL                                                # Modifying Font Type
        cv2.putText(icon, TxtBCHFile, (a + 10, b - 10), TxtFont, 1.0, (150, 150, 150), 2)       # Layout and Text Color for the Font Presets.
        cv2.putText(icon, TxtBCHFile, (a + 10, b - 10), TxtFont, 1.0, (150, 0, 0), 2)           # Layout and Text Color for the Font Presets.
        """
        TEXT FILE WITHIN THE SAME FOLDER HAS THE AUTHORIZATION TO GET OVERWRITTEN.
        """
        local_time = datetime.now()                                                             # REAL-TIME GMT+8 / UTC+9 PHILIPPINES
        datezone = local_time.strftime("%B %d, %Y")                                             # MONTH, DAY, AND YEAR (e.g. January 1, 2022)
        current_time = time.localtime()                                                         # The Localtime will be Detected - MANILA, PHL
        timezone = time.strftime("%H:%M", current_time)                                         # HOURS AND MINUTES (e.g. 09:45) with regards to AM and PM
        timezoneNUM = int(time.strftime("%H", current_time))                                    # Disregarding the 24 Hour Clock
        timezoneDate = time.strftime("%M", current_time)                                           # A Full-Hour Minute (60 Minutes)
        hour_clock = 12
        with open(details, "w", encoding="utf-8") as update:
            if timezoneNUM >= 0 and timezoneNUM < hour_clock:
                update.write(TxtBCHFile + (f"\n\n>>> RECORD OF SCANS <<< \nDate Tracking Record: {datezone}\nTime Tracking Record: {timezone} AM"))
            else:
                timeCurrent = (timezoneNUM) - hour_clock
                update.write(TxtBCHFile + (f"\n\n>>> RECORD OF SCANS <<< \nDate Tracking Record: {datezone}\nTime Tracking Record: {timeCurrent}:{timezoneDate} PM"))
    return icon;                                                                                # Brings back the variable upon the Font Layout - illustration on the Live Webcam.
details = "record of scans.txt"
