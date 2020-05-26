# GetFileInfo
## go through all the folders
os.walk(folder_path)
## get paths of a certain file type
conditional judgement
file.endswith('.pdf') and 'certainSubstring' in file
## get certain info about a file
1. full path + file name
   - os.path.join()
2. file size
   - os.path.getsize()
3. file most recent edited time
   - get certain time info of the file
     - info=os.stat(file_path)
   - convert the second format into local date frame
     - time.ctime(info.st_mtime)
## store the file information in a csv file
### write several columns
1. zip several parts of the fileinfo into a rows matrix
  - each row has full path as col1, file name as col2, filesize as col3, timestamp as col4
    - rows= zip(list1,list2,list3)
2. write into a csv file using csv module
  - open('filename','w',encoding='utf-8') as f
  - wr= csv.writer(f)
  - wr.writerow(row)




