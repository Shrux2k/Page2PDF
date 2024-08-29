Here's a `README.md` file for your script, including a backstory on why you made it and instructions on how to use it:

---

## Page2PDF

### Overview

**Page2PDF** is a Python script designed to convert any webpage into a PDF or Word document. It saves the converted files into organized folders (`PDF` and `Word`) based on the selected output format. The filenames are automatically generated based on the website's domain name, ensuring each file is uniquely named and easily identifiable.

I created this script out of a need to easily save and organize content from various webpages for offline reading and research purposes. Often, I found myself needing to keep track of articles, tutorials, or other resources from the web, but manually saving each page was tedious and disorganized. Thus, I developed **Page2PDF** to automate the process, ensuring that all saved content is systematically named and stored, making it easy to access later.

### Features

- **Convert Webpages to PDF or Word**: Choose to save any webpage as a PDF or a Word document.
- **Automatic Folder Organization**: Saves files into dedicated `PDF` and `Word` directories.
- **Unique Filenames**: Generates filenames based on the domain name of the webpage to avoid overwriting files and to keep everything organized.

### Prerequisites

Before you can use this script, you need to have the following Python libraries installed:

- `requests`
- `pdfkit`
- `beautifulsoup4`
- `python-docx`
- `wkhtmltopdf` (external tool)

To install the required Python libraries, run:

```bash
pip install requests pdfkit beautifulsoup4 python-docx
```

For `wkhtmltopdf`, install it using your package manager or download it from the [wkhtmltopdf download page](https://wkhtmltopdf.org/downloads.html).

### Installation

1. **Clone the repository** (or save the script file to your local machine).
   
   ```bash
   git clone https://github.com/yourusername/Page2PDF.git
   cd Page2PDF
   ```

2. **Install the required libraries**:

   ```bash
   pip install -r requirements.txt
   ```

   *(Note: You'll need to create a `requirements.txt` file containing the library names, or you can manually install them as listed above.)*

3. **Install `wkhtmltopdf`** using your system's package manager or from the official website.

### Usage

To convert a webpage to PDF or Word format, use the script from the command line:

```bash
python3 Page2PDF.py <url> [--pdf] [--word]
```

- `<url>`: The URL of the webpage you want to convert.
- `--pdf`: Optional flag to save the webpage as a PDF.
- `--word`: Optional flag to save the webpage as a Word document.

#### Examples

1. To save a webpage as a PDF:

   ```bash
   python3 Page2PDF.py https://www.example.com --pdf
   ```

2. To save a webpage as a Word document:

   ```bash
   python3 Page2PDF.py https://www.example.com --word
   ```

### Output

- PDFs are saved in the `PDF` directory.
- Word documents are saved in the `Word` directory.
- Filenames are automatically generated based on the domain name of the URL.

### Troubleshooting

- **No `wkhtmltopdf` executable found**: Make sure `wkhtmltopdf` is installed and accessible from your system's PATH.
- **ModuleNotFoundError**: Install any missing Python libraries using pip.

### Contributing

If you have suggestions for improvements or encounter any issues, feel free to open an issue or create a pull request. Contributions are welcome!

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Acknowledgements

Special thanks to the developers of `pdfkit`, `BeautifulSoup`, `python-docx`, and `requests` for providing the essential tools needed for this script.

---

Feel free to modify this `README.md` as needed to fit your project and personal style!
