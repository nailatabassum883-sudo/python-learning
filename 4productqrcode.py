import qrcode
data=input("Enter text or URL:")
qr=qrcode.make(data)
qr.save("My_QR_Code.png")
print("QR Code Created successfully!")
