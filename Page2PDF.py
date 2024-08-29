import argparse
import os
import requests
import pdfkit
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from docx import Document

def generate_filename_from_url(url, extension):
    # Parsing the URL to extract the domain name
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.replace('.', '_')
    filename = f"{domain}.{extension}"
    return filename

def save_as_pdf(url):
    try:
        os.makedirs('PDF', exist_ok=True)
        output_file = generate_filename_from_url(url, 'pdf')
        output_path = os.path.join('PDF', output_file)
        pdfkit.from_url(url, output_path)
        print(f"PDF saved as {output_path}")
    except Exception as e:
        print(f"Failed to save PDF: {e}")

def save_as_word(url):
    try:
        os.makedirs('Word', exist_ok=True)
        output_file = generate_filename_from_url(url, 'docx')
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        document = Document()

        # Extracting text content from paragraphs and headings
        for element in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            document.add_paragraph(element.get_text())

        output_path = os.path.join('Word', output_file)
        document.save(output_path)
        print(f"Word document saved as {output_path}")
    except Exception as e:
        print(f"Failed to save Word document: {e}")

def main():
    parser = argparse.ArgumentParser(description='Convert a webpage to PDF or Word document.')
    parser.add_argument('url', type=str, help='URL of the webpage to convert')
    parser.add_argument('--pdf', action='store_true', help='Convert to PDF')
    parser.add_argument('--word', action='store_true', help='Convert to Word document')
    args = parser.parse_args()

    if not args.pdf and not args.word:
        print("Please specify --pdf or --word.")
        return

    if args.pdf:
        save_as_pdf(args.url)

    if args.word:
        save_as_word(args.url)

if __name__ == '__main__':
    main()
