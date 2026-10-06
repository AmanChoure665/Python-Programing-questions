"""
Q101. File Type Check

Take a filename as input (like report.pdf). Check if it ends with .pdf, .docx,
or .txt and print the file type.
"""
def check_filename(filename):
    filename = filename.split(".")

    if filename[1] == "pdf":
        return f"It's an PDF file"
    elif filename[1] == "docx":
        return f"It's an docx(document) file"
    elif filename[1] == "txt":
        return f"It's an text file"
    else:
        return "It's an invalid filetype"

filename = input("Enter file name: ")
print(check_filename(filename))