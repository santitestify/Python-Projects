from barcode import EAN13
from barcode.writer import ImageWriter

num_of_barcodes = int(input("how many barcodes you need: "))
numbers = range(num_of_barcodes)

for i in numbers:
    # make sure to pass the number as string
    ID = input(" Give 12-digit number for your barcode id: ")
    # Now, let's create and object of EAN13
    # class and pass the number
    my_code = EAN13(ID, writer=ImageWriter())

    # Our barcode is ready. let's save it
    name = input(" Give the name to save barcodes: ")
    my_code.save(name)


