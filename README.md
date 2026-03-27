# File Parser & Converter (Python CLI Tool)

![Language](https://img.shields.io/badge/Language-Python-blue)
![Libraries](https://img.shields.io/badge/Libraries-pandas%20%7C%20PyPDF2%20%7C%20python--docx-orange)
![Interface](https://img.shields.io/badge/Interface-CLI-lightgrey)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

---

## Overview

This project is a **command-line file parser and converter** written in Python.
It supports multiple file formats and provides a wide range of operations including reading, analyzing, modifying, converting, and managing files.

The tool is designed to demonstrate:

* File handling across multiple formats
* Modular programming
* Functional decomposition
* Real-world utility scripting

---

## Supported File Types

* `.txt` (Text files)
* `.pdf`
* `.docx` / `.doc`
* `.csv`

---

## Features

### Core Functionality

* Read and display file contents
* Count:

  * Characters
  * Words
  * Lines
* Search for patterns within files
* Replace text (single or multiple occurrences)
* Copy files
* Delete files
* Display file metadata

---

### File Conversion

* PDF → TXT
* TXT → PDF
* DOCX → TXT
* TXT → DOCX
* DOCX → PDF
* PDF → DOCX

---

### CSV-Specific Features

* Display CSV data using pandas
* Count:

  * Characters
  * Words
  * Cells
* Replace values in CSV files
* Display CSV structure:

  * Columns
  * Data types
  * Sample rows

---

### Additional Features

* File type detection using file signatures
* Interactive CLI menus
* Directory browsing (`list` / `dir`)
* Typewriter-style output for improved UX
* Error handling and input validation

---

## Project Structure

```bash
.
├── sanmisFileParser.py   # Main program entry point
├── fp_func_file.py       # Core file handling and utilities
├── csv_parser.py         # CSV-specific functionality
└── README.md             # Documentation
```

---

## How It Works

1. User launches the program
2. Inputs a file name
3. System detects file type automatically
4. Displays a menu of available operations
5. Executes selected actions based on file type

---

## How to Run

### Prerequisites

Install required dependencies:

```bash
pip install pandas python-docx PyPDF2 pymupdf pypandoc fpdf pdfminer.six
```

---

### Run the Program

```bash
python sanmisfileparser.py
```

---

## Example Workflow

```text
Enter file name: sample.txt

Enter action:
1 -> Read file
2 -> Count words/characters
3 -> Count lines
4 -> Search
5 -> Replace
...
```

---

## Design Highlights

### Modularity

* Separated logic across multiple files:

  * Core utilities (`fp_func_file.py`)
  * CSV handling (`csv_parser.py`)
  * Main controller (`sanmisfileparser.py`)

### Reusability

* Functions are reusable across different file types
* Conversion utilities shared across modules

### User Experience

* Interactive CLI menus
* Typewriter-style output simulation
* Clear prompts and feedback

---

## Limitations

* CLI-only interface
* No GUI support
* Large files may affect performance
* Limited validation for malformed CSV files

---

## Future Improvements

* Implement GUI (Tkinter or PyQt)
* Add support for more file formats (e.g., JSON, XML)
* Improve performance for large datasets
* Add logging system
* Implement unit testing
* Add batch file processing

---

## Author

Oluwasanmi Longe
GitHub: https://github.com/sanmilonge

---

## License

This project is intended for educational purposes only.

---
