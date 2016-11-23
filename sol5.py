import os
import datetime


#get the files in current directory
files = os.listdir()
name = str(datetime.datetime.now())+".txt"

#function that will merge
def merge_files(thefile):
   
   sourcefile=open(thefile, "r")
   content=sourcefile.read()
   with open(str(name), "a") as file:
       file.write(content+"\n")
       file.close()
   sourcefile.close()

#iterate to all files 
for i in files:
    if ".txt" in i:
        merge_files(i)




