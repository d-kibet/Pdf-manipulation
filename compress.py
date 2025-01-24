import fitz # PyMuPDF

def optimize_pdf(input_file, output_file):
    pdf_document = fitz.open(input_file)
    pdf_document.save(output_file, garbage=3, deflate=True)
    print(f"Optimized PDF file is saved as {output_file}")


#Let's use the above function
optimize_pdf('merged.pdf', 'optimized.pdf') 