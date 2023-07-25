# PDF Combiner

PDF Combiner is a Python script that allows you to merge multiple PDF files into a single combined PDF file. It uses the PyPDF2 library to perform the merging operation.

## Prerequisites

Before running the PDF Combiner script, make sure you have the following installed:

- Python 3.x
- PyPDF2 library (Install using `pip install PyPDF2`)
- colorama library (Install using `pip install colorama`)

## Usage

1. Clone the repository or download the `pdfCombine.py` file.

2. Put the PDF files you want to combine in a specific folder.

3. Open the terminal (or command prompt) and navigate to the folder where the `pdfCombine.py` script is located.

4. Run the script using the following command:

python pdfCombine.py

Make sure to modify the `pdfCombine.py` script to set the correct `input_folder_path` and `output_folder_path` variables based on the location of your PDF files and the desired output folder.

5. The script will then merge all the PDF files in the input folder and create a new combined PDF file in the specified output folder.

6. After the process is completed, you will see a success message with the path of the combined PDF file displayed in green.

## Note
* The script only combines files that have the .pdf extension.
* Ensure that you have the required permissions to read the input files and write to the output folder.
* Always double-check the output folder path to avoid accidental overwriting of existing files.

