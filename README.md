# PDF Manipulation with Python

## 📖 Project Overview
This project demonstrates how to perform basic and advanced PDF manipulation tasks using Python. It provides functionality to merge, split, encrypt, decrypt, edit metadata, extract data from various PDFs, and optimize PDFs using the `PyPDF2` library. This is a versatile tool for managing and processing PDF files for various use cases.

---

## ✨ Features
- **Merge PDFs**: Combine multiple PDF files from a folder into a single PDF.
- **Split PDFs**: Split a single PDF into separate files, each containing individual pages or ranges of pages.
- **Encrypt PDFs**: Add password protection to PDFs for security.
- **Decrypt PDFs**: Remove password protection from encrypted PDFs (if the password is known).
- **Edit Metadata**: Modify or add metadata like title, author, subject, and keywords in PDF files.
- **Extract Data**: Extract text or images from PDF files.
- **Optimize PDFs**: Reduce the file size of PDFs by compressing images and removing unnecessary elements.
- **Automatic Sorting**: Merges or processes files in alphabetical order for consistent output.
- **Efficient and Lightweight**: Uses the Python library `PyPDF2` for seamless PDF handling.

---

## 🚀 How to Use the Project

### 1. Clone the Repository
First, clone the repository from GitHub:
```bash
git clone https://github.com/d-kibet/pdf-manipulation-python.git
```

Navigate into the project folder:
```bash
cd pdf-manipulation-python
```

---

### 2. Install Dependencies
Ensure you have Python installed on your machine. Then, install the required library `PyPDF2`:
```bash
pip install PyPDF2
```

---

### 3. Organize Your PDF Files
Place the PDF files you want to manipulate in a folder. By default, this project looks for PDF files in a folder named `pdf_files` within the project directory. You can change this in the code if needed.

---

### 4. Run the Script
Run the script to perform the desired PDF operation:
- **Merge PDFs**:
```bash
python merge_pdfs.py
```
- **Split PDFs**:
```bash
python split_pdfs.py
```
- **Encrypt PDFs**:
```bash
python encrypt_pdfs.py
```
- **Decrypt PDFs**:
```bash
python decrypt_pdfs.py
```
- **Edit Metadata**:
```bash
python edit_metadata.py
```
- **Extract Data**:
```bash
python extract_data.py
```
- **Optimize PDFs**:
```bash
python optimize_pdfs.py
```

---

### 5. Output
The resulting PDF files (merged, split, encrypted, decrypted, etc.) will be saved in the specified output folder or location, depending on the operation.

---

## 🛠 Customization
You can customize the script to suit your needs:
- **Input Folder**: Change the `input_folder` variable in the script to point to your folder containing the PDFs.
- **Output File Name**: Modify the `output_pdf` variable to set a different name or location for the output PDF.
- **Operation Parameters**: Adjust settings like encryption passwords, page ranges for splitting, or metadata fields.

---

## 📂 Folder Structure
```
pdf-manipulation-python/
│
├── pdf_files/          # Folder where you place the PDFs to manipulate
├── merge_pdfs.py       # Script for merging PDF files
├── split_pdfs.py       # Script for splitting PDF files
├── encrypt_pdfs.py     # Script for encrypting PDF files
├── decrypt_pdfs.py     # Script for decrypting PDF files
├── edit_metadata.py    # Script for editing metadata in PDFs
├── extract_data.py     # Script for extracting data from PDFs
├── optimize_pdfs.py    # Script for optimizing PDFs
├── README.md           # Documentation
└── requirements.txt    # List of dependencies
```

---

## 🖥 Requirements
- Python 3.7 or higher
- Libraries:
  - PyPDF2 (`pip install PyPDF2`)
  - PyMuPDF (`pip install PyMuPDF`)

---

## 📜 License
This project is licensed under the [MIT License](LICENSE).

---
