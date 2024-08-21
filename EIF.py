import fitz  # PyMuPDF
import pandas as pd

# Open the PDF file
pdf_document = fitz.open('/Users/apple/Downloads/eif-backed-active-funds.pdf')

# Initialize an empty list to hold the text
text_list = list()
headers_data = {
    0: "Location",
    1: "Fund Name",
    2: "Fund Manager",
    3: "Sector",
    4: "Fund Status",
    5: "End of investment period"
}
# Loop through each page and extract text
for page_num in range(len(pdf_document)):
    page = pdf_document.load_page(page_num)
    text = page.get_text()
    array = text.split("\n")
    result_dict = dict()

    row_data = dict()
    for i, value in enumerate(array):

        index = (i - 2) % 6

        if i == 0 or i == 1:
            continue

        header_name = headers_data[(i - 2) % 6]
        row_data[header_name] = value

        if index == 5:
            print(row_data)
            text_list.append(row_data)
            row_data = dict()
            print("==================")

# Create a DataFrame from the list
df = pd.DataFrame(text_list)

# Save the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)
