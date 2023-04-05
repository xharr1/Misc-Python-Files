import os
from PyPDF2 import PdfFileMerger
import time

curDate = time.strftime('%Y%m%d')
rootdir = 'C:/Example/Merge'

for subdir, dirs, files in os.walk(rootdir):
    for currentPDF in files:
        merger = PdfFileMerger()
        endName = os.path.join(currentPDF)
        print ("File is: " + endName)
        input1temp = 'C:/Example/Merge/' + endName
        input2temp = 'C:/Example/Pages to append.pdf'
        input1 = open(input1temp, "rb")
        input2 = open(input2temp, "rb")
        merger.append(fileobj=input1, pages=(0,1))
        merger.append(fileobj=input2, pages=(0,12))
        outputfile = 'C:/Example/Merge/To Batch/' + endName

        output = open(outputfile, "wb")
        merger.write(output)
        output.close()

        #clear all inputs
        outputfile = []
        output = []
        merger.inputs = []
        input1temp = []
        input2temp = []
        input1 = []
        input2 = []

print ("done")
