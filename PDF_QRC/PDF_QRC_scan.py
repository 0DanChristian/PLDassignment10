# Assignment 10

#   Contact Tracing App
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


# import Library
import cv2
import datetime
from pyzbar.pyzbar import decode
import qrcode
import webbrowser


# capture vid
capture_vid = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

# generate qr
img = qrcode.make('PDF_Trace.pdf')
img.save('trace_qr.png')

# Scan
QR_scanner = True

while QR_scanner == True:
    captured, img = capture_vid.read()
    data, one, _ = detector.detectAndDecode(img)
    if data:
        read = data
        # Record Date and Time of QR Code Detection
        with open("record_of_scans.txt", mode='a') as file:
            file.write(f'Scanned QR Code redirecting to {read} recorded at %s.\n' % 
               (datetime.datetime.now()))
        break
    
    for scanned_QR in decode(img):
        text = scanned_QR.data.decode('utf-8')
        print(text)

        # record
        with open("record_of_scans.txt", mode='a') as file:
            file.write(f'Scanned QR Code containing {text} was recorded at %s.\n' % 
            (datetime.datetime.now())) 
            capture_vid.release(text)
            cv2.destroyAllWindows
        break

    cv2.imshow('Dan Christian QRC Scanner', img)
    if cv2.waitKey(1)==ord('a'):
        break
    
redirect = webbrowser.open((str(read)))
capture_vid.release(read)
cv2.destroyAllWindows
