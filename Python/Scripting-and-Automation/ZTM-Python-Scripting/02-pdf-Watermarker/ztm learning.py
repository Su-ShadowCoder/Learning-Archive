# Following the lecture code notes

import pypdf

pdf_input = pypdf.PdfReader(open('super.pdf', 'rb'))

watermarker = pypdf.PdfReader(open('wtr.pdf', 'rb'))

pdf_output = pypdf.PdfWriter()

for page in pdf_input.pages:
    page.merge_page(watermarker, over=True)
    pdf_output.add_page(page)

with open("watermarked-pdf-02.pdf", 'wb') as outputFile:
    pdf_output.write(outputFile)












#lecture example:
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



