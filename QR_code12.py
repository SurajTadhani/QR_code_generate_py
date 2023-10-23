import qrcode
from PIL import _imaging

qr =qrcode.QRCode(version=1,
                  error_correction=qrcode.constants.ERROR_CORRECT_H,
                  box_size=8,border=3,)
qr.add_data("https://www.youtube.com/")

qr.make(fit=True)

img =qr.make_image(fill_color="black",back_color="blue")
img.save("QR_Color.png")