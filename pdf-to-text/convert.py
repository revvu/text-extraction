# Reevu Adakroy
# Script to convert pdfs into a .txt file
# Eventually this project will grow to include general text extraction.

'''
Mechanism: Produces page-by-page images from pdf. Runs OCR with context-based 
correction on each image. Inter-page context is lost.  
'''

# Notes: Handwritten characters will also be converted to text. 