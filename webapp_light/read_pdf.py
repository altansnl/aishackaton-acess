from pdfreader import PDFDocument, SimplePDFViewer

# get raw document
file_name = "sample_paper.pdf"
fd = open(file_name, "rb")
doc = SimplePDFViewer(fd)

full_str = ""
for page in doc:
    full_str += " ".join(page.strings)

print(full_str)
