'''import pdfkit

def convert_webpage_to_pdf(url, pdf_file):
    # Configure PDF options
    options = {
        'page-size': 'A4',
        'dpi': 400,
    }
    
    # Specify wkhtmltopdf path manually
    config = pdfkit.configuration(wkhtmltopdf="C:/path/to/wkhtmltopdf.exe")
    
    # Convert webpage to PDF
    pdfkit.from_url(url, pdf_file, options=options, configuration=config)
    print("Webpage converted to PDF successfully.")

# Example usage:
url = "https://www.somaiya.edu/en/contact-us/contact-directory/"
pdf_file = "output.pdf"
convert_webpage_to_pdf(url, pdf_file)
'''

