import barcode
import os.path

from barcode.writer import ImageWriter

number = input("Enter barcode number: ")
writer = ImageWriter()
barcode = barcode.get_barcode_class("code128")
barcode(number, writer=writer).save(f"images/barcode{sum(os.path.isfile(os.path.join("images", f)) for f in os.listdir("images"))}")