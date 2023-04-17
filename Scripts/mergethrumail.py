import os
import shutil
import uuid
import imaplib
import email
from pdfrw import PdfReader, PdfWriter


imap_url = "imap.gmail.com"
username = "your_email@example.com"
password = "your_password"
attachment_folder = "C:/Users/tonyd/Desktop/PDFS"

# Connect to email and select the mailbox
mail = imaplib.IMAP4_SSL(imap_url)
mail.login(username, password)
mail.select('inbox')  # Select the 'inbox' mailbox


_, message_numbers = mail.search(None, 'ATTACHMENT')

pdfs = []
specific_pdfs = ['file1.pdf', 'file2.pdf']
for msg_num in message_numbers[0].split():
    _, msg_data = mail.fetch(msg_num, '(RFC822)')
    raw_email = msg_data[0][1]
    msg = email.message_from_bytes(raw_email)
    for part in msg.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue

        filename = part.get_filename()
        if filename.endswith('.pdf') and filename in specific_pdfs:
            file_path = os.path.join(attachment_folder, filename)
            pdfs.append(file_path)
            with open(file_path, 'wb') as f:
                f.write(part.get_payload(decode=True))


writer = PdfWriter()
for pdf in pdfs:
    reader = PdfReader(pdf)
    writer.addpages(reader.pages)

result_pdf = os.path.join(attachment_folder, f"result_{uuid.uuid4().hex}.pdf")
with open(result_pdf, "wb") as f:
    writer.write(f)

read_folder = os.path.join(attachment_folder, "read")
if not os.path.exists(read_folder):
    os.makedirs(read_folder)

for pdf in pdfs:
    unique_filename = f"{os.path.splitext(os.path.basename(pdf))[0]}_{uuid.uuid4().hex}.pdf"
    unique_path = os.path.join(read_folder, unique_filename)
    shutil.move(pdf, unique_path)  # Move the PDFs to the "read" folder.
    # os.remove(pdf)  # Uncomment this line and comment the line above to delete the PDFs instead of moving them.

mail.logout()
