# Read the metadata of the PDF file
import PyPDF2

def read_metadata(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    metadata = pdf_reader.metadata

    print ("Metadat of the PDF file is:")
    for key, value in metadata.items():
        print(f"{key}: {value}")


#Let's use the above function
read_metadata('merged.pdf') 