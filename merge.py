import PyPDF2
from pathlib import Path
from typing import Union, Literal, List
from PyPDF2 import PdfWriter, PdfReader

def pmergr():
    pdfile = ["1.pdf","2.pdf"]
    merger = PyPDF2.PdfMerger()
    for filename in pdfile:
        pdfFile = open(filename,'rb')
        pdfReader = PyPDF2.PdfReader(pdfFile)
        merger.append(pdfReader)
    pdfFile.close()
    merger.write('merged.pdf')
print("Files are sucessfully Merged....!")
def pextract():
    reader = PdfReader("1.pdf")
    page = reader.pages[0]
    print(page.extract_text())
    print(page.extract_text(0))
    # extract text oriented up and turned left
    print(page.extract_text((0, 90)))
print("File Text is sucessfully extracted ")
def stamp(
    content_pdf: Path,
    stamp_pdf: Path,
    pdf_result: Path,
    page_indices: Union[Literal["ALL"], List[int]] = "ALL",
):
    reader = PdfReader(stamp_pdf)
    image_page = reader.pages[0]

    writer = PdfWriter()

    reader = PdfReader("1.pdf")
    if page_indices == "ALL":
        page_indices = list(range(0, len(reader.pages)))
    for index in page_indices:
        content_page = reader.pages[index]
        mediabox = content_page.mediabox
        content_page.merge_page(image_page)
        content_page.mediabox = mediabox
        writer.add_page(content_page)

    with open(pdf_result, "wb") as fp:
        writer.write(fp)
print("Stamped....")
def watermark(
    content_pdf: Path,
    stamp_pdf: Path,
    pdf_result: Path,
    page_indices: Union[Literal["ALL"], List[int]] = "ALL",
):
    reader = PdfReader("2.pdf")
    if page_indices == "ALL":
        page_indices = list(range(0, len(reader.pages)))

    writer = PdfWriter()
    for index in page_indices:
        content_page = reader.pages[index]
        mediabox = content_page.mediabox

        # You need to load it again, as the last time it was overwritten
        reader_stamp = PdfReader(stamp_pdf)
        image_page = reader_stamp.pages[0]

        image_page.merge_page(content_page)
        image_page.mediabox = mediabox
        writer.add_page(image_page)

    with open(pdf_result, "wb") as fp:
        writer.write(fp)
print("Watermark is Added....")

def reducesize():
    reader = PdfReader("1.pdf")
    writer = PdfWriter()
    for page in reader.pages:
        page.compress_content_streams()  # This is CPU intensive!
        writer.add_page(page)
    with open("out.pdf", "wb") as f:
        writer.write(f)
print("Its Done....")

