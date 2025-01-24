# Removing Passwords from the password protected PDFs
import PyPDF2

def decrypt_pdf(input_pdf, output_pdf, password):
    pdf_reader = PyPDF2.PdfReader(input_pdf)
    pdf_reader.decrypt(password)
    pdf_writer = PyPDF2.PdfWriter()


    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])

    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)

    print(f"Decrpted PDF file is saved as {output_pdf}")


# Let'suse the above function
decrypt_pdf('encrypted.pdf', 'decrypted.pdf', 'pass123')