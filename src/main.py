import barcode

from barcode.writer import ImageWriter

number = input("Enter barcode number: ")
writer = ImageWriter()
barcode = barcode.get_barcode_class("code128")
barcode(number, writer=writer).save("barcode.png")