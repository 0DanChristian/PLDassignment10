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

encode.add_data(details)
# QR Code Presets and Illustrative Design for the making of PNG File.
encode.make(fit = True); icon = encode.make_image(back_color = 'white', fill_color = 'black').convert('RGB')
# The QR code will be saved from its Python Settings upon the dictation of the naming file.
"""
LOGO IMAGE HEADER FOR THE QR CODE PNG FILE (DESIGN PURPOSES)
"""
logo_display = Image.open('WHO.png') # PNG is imported through Image module.
logo_display.thumbnail((180, 180)) # Aspect Ratio of the imported PNG File.
logo_pos = ((icon.size[0] - logo_display.size[0]) // 2, (icon.size[1] - logo_display.size[1]) // 2) # Image Size Presets has been customized.
icon.paste(logo_display, logo_pos) # PNG is displayed through the "icon" global variable.
# The QR code will be saved from its Python Settings upon the dictation of the naming file.
icon.save('DAN_QRC.png')

# with Villariza's guide in this code I was able to understand generating QRC using python :>>