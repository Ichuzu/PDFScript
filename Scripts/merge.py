#med libraries

# import os
# import PyPDF2

# folder_path = 'C:/Users/tonyd/Desktop/PDFS'
# pdfs = []

# for file in os.listdir(folder_path):
#     if file.endswith('.pdf'):
#         pdfs.append(os.path.join(folder_path, file))


# merger = PyPDF2.PdfFileMerger()
# for pdf in pdfs:
#     merger.append(open(pdf, 'rb'))

# with open(os.path.join(folder_path, "result.pdf"), "wb") as f:
#     merger.write(f)

# merger.close()





#testa utan libraries
#och kastar pdf som är använt i en fil kallat finnished
# import os
# import shutil
# from pdfrw import PdfReader, PdfWriter

# readpdfs = 'C:/Users/tonyd/Desktop/PDFS'
# pdfs = []

# for file in os.listdir(readpdfs):
#     if file.endswith('.pdf'):
#         pdfs.append(os.path.join(readpdfs, file))

# writer = PdfWriter()
# for pdf in pdfs:
#     reader = PdfReader(pdf)
#     writer.addpages(reader.pages)

# with open(os.path.join(readpdfs, "result1.pdf"), "wb") as f:
#     writer.write(f)

#     finished_folder = os.path.join(readpdfs, "finished")
# if not os.path.exists(finished_folder):
#     os.makedirs(finished_folder)

# for pdf in pdfs:
#     shutil.move(pdf, finished_folder)




#skapar en read fil. eller så kan den radera bort de
# import os
# import shutil
# from pdfrw import PdfReader, PdfWriter

# readpdfs = 'C:/Users/tonyd/Desktop/PDFS'
# pdfs = []

# # List specific PDF filenames here, e.g., ['file1.pdf', 'file2.pdf', 'file3.pdf']
# specific_pdfs = ['file1.pdf', 'file2.pdf']

# for file in os.listdir(readpdfs):
#     if file.endswith('.pdf') and file in specific_pdfs:
#         pdfs.append(os.path.join(readpdfs, file))

# writer = PdfWriter()
# for pdf in pdfs:
#     reader = PdfReader(pdf)
#     writer.addpages(reader.pages)

# with open(os.path.join(readpdfs, "result.pdf"), "wb") as f:
#     writer.write(f)

# read_folder = os.path.join(readpdfs, "read")
# if not os.path.exists(read_folder):
#     os.makedirs(read_folder)

# for pdf in pdfs:
#     shutil.move(pdf, read_folder)  # Move the PDFs to the "read" folder.
#     # os.remove(pdf)  # Uncomment this line and comment the line above to delete the PDFs instead of moving them.




import os
import shutil
import uuid
from pdfrw import PdfReader, PdfWriter

readpdfs = 'C:/Users/tonyd/Desktop/PDFS'
finished_folder = 'C:/Users/tonyd/Desktop/PDFS/finished' 

if not os.path.exists(finished_folder):
    os.makedirs(finished_folder)

pdfs = []

for file in os.listdir(readpdfs):
    if file.endswith('.pdf'):
        pdfs.append(os.path.join(readpdfs, file))

writer = PdfWriter()
for pdf in pdfs:
    reader = PdfReader(pdf)
    writer.addpages(reader.pages)

# Generate a unique filename for the result PDF
result_pdf = os.path.join(finished_folder, f"result_{uuid.uuid4().hex}.pdf")
with open(result_pdf, "wb") as f:
    writer.write(f)

for pdf in pdfs:
    # Generate a unique filename for the processed PDF
    unique_filename = f"{os.path.splitext(os.path.basename(pdf))[0]}_{uuid.uuid4().hex}.pdf"
    unique_path = os.path.join(unique_filename)
    os.remove(pdf)  # Uncomment this line and comment the line above to delete the PDFs instead of moving them.
