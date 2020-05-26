# read in the file information
# write into a csv file
# Modules needed: os,csv,time

import os
import time
import csv

FOLDER_PATH=r'C:\Users\jinxi\Documents\JobApplication'
if __name__ == '__main__':

    allpath=[]
    allfilename=[]
    allsize=[]
    allinfo=[]

    for root_dir_path, sub_dirs, files in os.walk(FOLDER_PATH):
        for file in files:
            if file.endswith('.pdf') and 'Anschreiben' in file:
                file_path = os.path.join(root_dir_path, file)

                allpath.append(os.path.join(root_dir_path,file))
                allfilename.append(file)
                allsize.append(os.path.getsize(file_path))

                info=os.stat(file_path)
                allinfo.append(str(time.ctime(info.st_mtime)))

    rows = zip(allpath, allfilename,allsize, allinfo)
    with open('newCSV.csv','w',encoding='utf-8') as myfile:
        wr=csv.writer(myfile)
        for row in rows:
            wr.writerow(row)
        myfile.close()