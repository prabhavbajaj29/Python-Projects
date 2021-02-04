import pyqrcode
from pyqrcode import QRCode

# String which represent the QR Code
s="www.linkedin.com/in/prabhav-bajaj-199791200"

#Generate QR Code
url=pyqrcode.create(s)

# Create and save the png file naming "myqr.png" 
url.svg("my linkedin.svg",scale= 8)