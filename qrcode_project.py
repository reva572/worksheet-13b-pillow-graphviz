
import qrcode

data = "https://github.com/reva572/worksheet-13b-pillow-graphviz"

qr = qrcode.QRCode(
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="white")

img.save("my_qrcode.jpg")

print("QR code generated successfully!")
