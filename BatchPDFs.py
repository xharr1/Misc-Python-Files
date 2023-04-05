# needed to access PDFs from python:
from PyPDF2 import PdfFileMerger, PdfFileReader
 
# needed to read files in directory (dir) and exit on error:
import os, sys
 
# on my laptop it needed 10 min to merge 20000 pdfs with 1 page
import datetime
import time

# location of your PDFs (windows style), example:
dir_in = ('C:/Example/Merge/To Batch/')
os.chdir(dir_in)
 
# dir of the mergrf PDFs, here subdir from your PDF collection
dir_out = 'Batches'
 
# make sure only files ending with pdf are processed
pdfs = [name for name in os.listdir(dir_in) if name.endswith(".pdf")]
 
# check if dir exists, create if not, error if not possible
if os.path.exists(dir_out):
    pass
else:
    try:
        os.mkdir(dir_out)
    except OSError:
        print ("Could not create output dir %s " % dir_out)
        sys.exit(1)
    else:
        print ("Created output dir %s " % dir_out)
    
# remove pdfs from list if you like
 
# sort PDFs, they will be merged in this order
pdfs.sort(reverse=False) # or: reverse=True
print("Number of pdfs: " + str(len(pdfs)))
 
# holds a batch of pdf names
batch_pdfs = []
 
# collects all batches
list_of_batches= []
 
# make batches after this number of files
# you can change the batchsize here.
batchsize = 200
print("Batchsize: " + str(batchsize))
 
# Loop over the list with all pdf names 
# and split them into batches (=batch_pdfs).
# Collect each batch in list "list_of_batches".
for count, pdf in enumerate(pdfs, 1):        
    batch_pdfs.append(pdf)
    if count % batchsize == 0:
        list_of_batches.append(batch_pdfs)
        batch_pdfs = []
        
    # if you loop longer than the number of pdfs, something is wrong. exit.   
    if count > len(pdfs) + 2:
        print('List count larger than number of PDFs.')        
        os.sys.exit(1)
    
list_of_batches.append(batch_pdfs)
print("No of batches: "+str(len(list_of_batches)))

print(datetime.datetime.now())

i = 1
# loop over all batches (=list_of_batches)
for batchlist in list_of_batches:
    print("Processing Batch: " + str(i) + " with length: " + str(len(batchlist)))    
    if len(batchlist) > 0:
        # Start the PDF merger for each batch and close it after the batch.
        #  If you try to merge too many pdfs at once, you get a "too many open files" error.
        merger = PdfFileMerger()
        for pdf in batchlist:
            #print(pdf)
            try:
                with open(pdf, "rb") as file:                           
                    merger.append(PdfFileReader(file))
                    
                    #print(pdf)
                    
            except:
                print("error merging: " + pdf)
            time.sleep(0.2)
            os.rename('C:/Example/Merge/To Batch/Out/' + pdf,'C:/Example/Merge/To Batch/Out/Archive/' + pdf)
 
        # Close merger after the batch!
        merger.write(dir_out+"/"+"PDFName"+ time.strftime('%Y%m%d%H%M%S') +".pdf")
        merger.close()
        print(datetime.datetime.now())
    i+=1
 
# friendly byebye to the user :-)
print('Check folder: \"'+ dir_out + '\" for PDFs.')
print('finished i have.')
