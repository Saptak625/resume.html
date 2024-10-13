from seleniumprint import url_to_pdf
import datetime

input_html_url="http://localhost:5500"
output_pdf_file_path=f"resume_{datetime.datetime.now().strftime('%m_%d_%Y')}.pdf"

try:
    url_to_pdf(input_html_url, output_pdf_file_path)
    print("PDF created successfully")
except Exception as e:
    print("Error creating PDF: ", e)