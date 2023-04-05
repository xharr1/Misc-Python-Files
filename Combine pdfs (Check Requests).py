import os
from PyPDF2 import PdfFileMerger
import time

curDate = time.strftime('%Y%m%d')
rootdir = 'C:/Example/Check Requests/' + curDate + '/Request'

for subdir, dirs, files in os.walk(rootdir):
    for currentPDF in files:
        merger = PdfFileMerger()
        pagename = os.path.join(currentPDF[0:7])
        endName = os.path.join(currentPDF)
        print ("pagename is: " + pagename)
        print ("File is: " + endName)
        input1temp = 'C:/Example/Check Requests/' + curDate + '/Request/' + endName
        input2temp = 'C:/Example/Check Requests/' + curDate + '/Backup/' + pagename + '_Backup.pdf'
        input1 = open(input1temp, "rb")
        input2 = open(input2temp, "rb")
        merger.append(fileobj=input1, pages=(0,1))
        merger.append(fileobj=input2, pages=(0,1))
        outputfile = 'C:/Example/Check Requests/' + curDate + '/' + endName

        print (merger.inputs)

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