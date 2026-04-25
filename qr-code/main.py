import qrcode

message = """Hello baby ❤️
I love you so much.
You are the very special person in my life.
You make my days beautiful, and I fall in love with you more every day 💕 I love you ❤️
"""

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(message)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("love_qr.png")
