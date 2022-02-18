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
