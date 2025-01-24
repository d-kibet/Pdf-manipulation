# Re-arranging pages in the PDF file.
import PyPDF2

def rearrange_pages(input_pdf, output_pdf, page_order):
    pdf_reader = PyPDF2.PdfReader(input_pdf)
    pdf_writer = PyPDF2.PdfWriter()

    for page_num in page_order:
        pdf_writer.add_page(pdf_reader.pages[page_num])

    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)

    print(f"Rearranged PDF is saved as {output_pdf}")


# Let's use the above function.
rearrange_pages('merged.pdf', 'rearranged.pdf', [2,1,0])

# [2,1,0] means file pages in reverse order