
# Meme Generator 

  A multimedia application to dynamically generate memes, including an image with an overlaid quote.


## Project Overview
 ### The Project :
- Interacts with a variety of complex filetypes.
- Loads quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files).
- Loads, manipulates, and saves images.
- Accepts dynamic user input through a command-line tool and a web service.
## Installation
There are two ways to run the application. 
- Running flask with app.py 
-- Run the code below in your terminal
```bash
 export FLASK_APP=app.py
flask run --host localhost --port 3000 --reload
```
Then navigate to the localhost on your browser

- Running python3 meme.py from your command line
```bash
--path path to the image
--body message for the meme
--author if available,author of the message

N.B- The three arguments are optional
```
 

    
## Description Of Modules And Sub-Modules
### QuoteEngine 
The code includes a Python class that defines a QuoteMode object, which contains text fields for body and author. The class overrides the correct methods to instantiate the class and print the model contents as: ”body text” - author

#### IngestorInterface
The project contains an abstract base class, IngestorInterface, which defines:
A complete classmethod method to verify if the file type is compatible with the ingestor class.
An abstract method for parsing the file content (i.e., splitting each row) and outputting it to a Quote object.

#### TextIngestor
The project contains a TextIngestor class, the class inherits the IngestorInterface.

#### CSVIngestor
The project contains a CSVIngestor class,the class inherits the IngestorInterface.The class depends on the pandas library to complete the defined, abstract method signatures to parse CSV files.

#### PDFIngestor
The project contains a PDFIngestor class,the PDFIngestor class inherits from the IngestorInterface class.
The PDFIngestor class utilizes the subprocess module to call the pdftotext CLI utility—creating a pipeline that converts PDFs to text and then ingests the text.

#### DOCXIngestor
The project contains a DocxIngestor class,the class inherits from the IngestorInterface class.
The class depends on the python-docx library to complete the defined, abstract method signatures to parse DOCX files.

### Dependencies
This can be found in the requirements' file
## Screenshots

[![meme-generator.jpg](https://i.postimg.cc/pV3S75pF/meme-generator.jpg)
![meme02.jpg](https://i.postimg.cc/cLRBFrn0/meme02.jpg)

