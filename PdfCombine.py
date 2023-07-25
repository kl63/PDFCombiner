import PyPDF2 # install library using "pip3 install PyPDF2"
import os
from colorama import Fore, Style

input_folder_path = "/Users/kevinlin192003/PDFCombiner/Input"  
output_folder_path = "/Users/kevinlin192003/PDFCombiner/Output"  

merger = PyPDF2.PdfMerger()

for file in os.listdir(input_folder_path):
    if file.endswith(".pdf"):
        file_path = os.path.join(input_folder_path, file) #Comebines only .pdf files in the Input folder
        merger.append(file_path)


output_path = os.path.join(output_folder_path, "combined.pdf") # Outputs the combined.pdf file in the OUTPUT folder
merger.write(output_path)
merger.close()  

print(Fore.GREEN + "MESSAGE: PDF files combined successfully! The combined file is saved at:", output_path) # Displays sucessful  merge message in terminal 
print(Style.RESET_ALL) 


""" Shell Script pdf.sh

#!/bin/zsh

cd /Users/kevinlin192003/PDFCombiner
python3 pdfCombine.py $1

"""
