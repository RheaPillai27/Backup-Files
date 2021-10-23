import os 
import shutil


listofFiles = os.listdir(source)
for file in listofFiles : 
    shutil.move((source + file),destination)