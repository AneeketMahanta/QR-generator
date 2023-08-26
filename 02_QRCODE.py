#Python Imaging Library (expansion of PIL)
#The fit() method takes the training data as arguments
import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)
qr.add_data("https://www.instagram.com/aneeket_mahanta/")
qr.make(fit=True)
img=qr.make_image(fill_colour="blue",back_colour="red")
img.save("aneeket_mahanta_instagram_web.png")