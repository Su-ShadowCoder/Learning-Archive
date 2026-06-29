

import os
import argparse
import pypdf
import sys


parser = argparse.ArgumentParser(description="A program that Watermarks all the pages of the pdf file")


parser.add_argument("source_pdf", help="Input: pdf file that needs to be watermarked")
parser.add_argument("destination_pdf", help="Output: Watermarked pdf file")
parser.add_argument("watermark_pdf", help="pdf file with the watermark")


args = parser.parse_args()

input_path = args.source_pdf
output_path = args.destination_pdf
watermark = args.watermark_pdf


if not os.path.exists(input_path):
    print(f"Error: {input_path} not found.")
    sys.exit(1)
else:
    print(f"Reading from:{input_path}")
    print(f"Saving to:{output_path}")


if not os.path.exists(watermark):
    print(f"Error: {watermark} not found.")
    sys.exit(1)
else:
    print(f"watermark from {watermark} found. processing!")

stamp = pypdf.PdfReader(watermark).pages[0]
writer = pypdf.PdfWriter(clone_from=input_path)
for page in writer.pages:
    page.merge_page(stamp, over=False)

writer.write(output_path)
writer.close()
