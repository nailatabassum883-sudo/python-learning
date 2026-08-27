import barcode
from barcode.writer import ImageWriter


product_name=input('Please enter your product name:')
product_id=input('Please enter your product id:')

code = barcode.get("code128",product_id,writer=ImageWriter())

code.save(product_name + "_Barcode")

print("Your barcode is ready to serve")
