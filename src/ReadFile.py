from xml.dom.minidom import Document

import PyPDF2 as PyPDF2


def read_file(filename):
    """
  This function reads the content of a file, handling text, PDF, and Word formats.

  Args:
      filename (str): The name of the file to read.

  Returns:
      str: The content of the file as a string (if readable).
  """

    # Check file extension and use appropriate method
    if filename.endswith(".txt"):
        with open(filename, 'r') as f:
            content = f.read()
    elif filename.endswith(".pdf"):
        try:
            with open(filename, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                content = ""
                for page_num in range(
                        len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    content += page.extract_text()
        except:
            print(f"Error reading PDF: {filename}")
            content = ""  # Set content to empty string on error
    elif filename.endswith(".docx"):
        try:
            doc = Document(filename)
            content = [p.text for p in doc.paragraphs]
            content = "\n".join(
                content)  # Join paragraph text with newlines
        except:
            print(f"Error reading Word doc: {filename}")
            content = ""  # Set content to empty string on error
    else:
        print(f"Unsupported file format: {filename}")
        content = ""  # Set content to empty string for unsupported formats

    return content.lower()  # Convert to lowercase for matching