# will use dictionary to generate QRC

import qrcode
from PIL import Image
"""
Lay out for Piñero's QRC png file.
"""
encode = qrcode.QRCode(
    # The general size of the QR Code.
    box_size = 8,
    # Alignment Pattern of the BCH Code.
    version = 1,
    # Distance from the QR Dataset Symbol Pattern
    border = 5,
    # Reed-Solomon Error Correction (H = High ) = 30% of data bytes can be stored.
    error_correction = qrcode.constants.ERROR_CORRECT_H 
)
"""
QRC generator layout
"""
# Data has been stored on the QR Code in an Alphanumeric Pattern.
# this is what will appear after scanning qrc.
details = """CONTACT TRACING  -  TOKYO, JAPAN

Personal Information
    Full Name       : Dan Christian Piñero
    Sex / Gender    : Male (M)
    Age             : 28
    Birthdate       : December 16, 1994
    Address         : 303-1069, Izumisawacho, Shiogama-shi, Miyag
    Phone Number    : +8137-422-2969
    Email           : danchristian1@gmail.com

Medical Information
    Weight (in kgs) : 55
    Height (in cms) : 5'7s

Symptoms

    Fever: 		None
    Cough: 		None
    Headache: 	None"""

