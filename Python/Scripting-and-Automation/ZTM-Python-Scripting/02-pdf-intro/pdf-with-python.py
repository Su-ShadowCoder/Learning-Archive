
from pypdf import PdfReader, PdfWriter

with open('dummy.pdf', 'rb') as file:
    reader = PdfReader(file)
    number_pages = len(reader.pages)
    first_page = reader.pages[0]
    
    # print(first_page.extract_text())
    # print(first_page)
    # print(number_pages(0))
    # print(dir(first_page))
    first_page.rotate(180)
    writer = PdfWriter()
    writer.add_page(first_page)
    with open("tilted.pdf", "wb") as new_file:
        writer.write(new_file)
        



    # print(f"Type of reader: {type(reader)}")
    # print(f"Type of first_page: {type(first_page)}")