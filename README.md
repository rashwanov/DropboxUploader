# DropboxUploader
Python script to automatically search windows for specific file types and upload them to dropbox

This script is used to automatically search the entire disk drive for a certain file types i.e: *.jpg and upload them to Dropbox

**usage:
          search-upload.py [manual\automatic] [Destination\file]
          
          search-upload.py automatic  # this will automatically search for all filetypes defined in def searcher():
          search-upload.py manual D:\\Folder\\"Sub Folder"\\*.pdf  # this will aupload all PDF files in certain location
          
