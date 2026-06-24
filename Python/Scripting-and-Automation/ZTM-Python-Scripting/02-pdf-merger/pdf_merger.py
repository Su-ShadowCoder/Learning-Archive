
from pypdf import PdfWriter

import sys


def merger():
    try:
        destination_file_name = sys.argv[1]
        sources_in_order = sys.argv[2:]
    except Exception:
        print("Something went wrong, please enter the correct files. Watch out for spelling mistakes!")
        sys.exit()
    merger = PdfWriter()
    for pdf in sources_in_order:
        merger.append(pdf)
    merger.write(destination_file_name)


def main():
	merger()


if __name__ == "__main__":
	main()




 





























######################################################
# Dont look, Excercise answer From teacher: 
######################################################
# import pypdf
 
# template = pypdf.PdfReader(open('superduper.pdf', 'rb'))
# watermark = pypdf.PdfReader(open('water.pdf', 'rb'))
# output = pypdf.PdfWriter()
 
# for i in range(len(template.pages)):
#     page = template.pages[i]
#     page.merge_page(watermark.pages[0])
#     output.add_page(page)
 
# with open('watermaked_output.pdf', 'wb') as outputFile:
#     output.write(outputFile)
######################################################

