

import os
import time
files = os.listdir()
if 'main.py' in files:
    files.remove('main.py')

files = [File for File in files if os.path.isfile(File)]


def createFolder(folderName):
    if not os.path.exists(folderName):
        os.makedirs(folderName)


def createListOfItems(ext):
    list_items = [File for File in files if os.path.splitext(File)[1] in ext]
    return list_items


def replaceFile(folderName, fileList):
    for item in fileList:
        os.replace(item, f"{folderName}/{item}")


def automateFolderCreate(folderName, fileList, typeofFile):
    if len(fileList) != 0:
        createFolder(folderName)
        replaceFile(folderName, fileList)
        print(f"\nGrouping : {fileList} as {typeofFile}")
        print(f"***Successfully! {len(fileList)} {typeofFile} files replaced to {folderName} Folder***")


if __name__ == "__main__":
    print("Proccessing...")
    time.sleep(1)
    print(f"Total {len(files)} files on this directory")
    if len(files) == 0:
        print("There are no files to arrange. All files already arranged.\nRun this program on another directory")
        a = input("Hit Enter to exit ")
        exit()
        
    print("Checking file types...")
    docExt = ['.doc', '.docx', 'docb', '.dotm', '.dot', '.xml', '.xps']
    docFiles = createListOfItems(docExt)

    powerPointExt = ['.pptx', '.pptm', '.potx', '.potm', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.ppt', '.pot', '.pps'] 
    powerPointFiles = createListOfItems(powerPointExt)
    
    oneNoteExt = ['one']
    oneNoteFiles = createListOfItems(oneNoteExt)
    
    excelExt = ['.xls', '.xlt', '.xlm', '.xlsx', '.xlsm', '.xltx', '.xltm', '.xlsb', '.xla', '.xlam', '.xll', '.xlw'] 
    excelFiles = createListOfItems(excelExt)
    
    accessExt = ['.accdb', '.accde', '.accdt', '.accdr']
    accessFiles = createListOfItems(accessExt)
    
    txtExt = ['.txt']
    txtFiles = createListOfItems(txtExt)

    imageExt = ['.jpg', '.jpeg', '.png','.gif', '.tif', '.tiff', '.eps', '.row']
    imageFiles = createListOfItems(imageExt)

    pdfExt = ['.pdf']
    pdfFiles = createListOfItems(pdfExt)

    compressesdExt = ['.zip', '.rar', '.z','.arj', '.deb', '.pkg', '.rpm', 'z', '.7z']
    compressesdFiles = createListOfItems(compressesdExt)
    
    mediaExt = ['.webm', '.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.ogg', '.mp4', '.mov', '.qt', '.flv', '.swf', '.avchd']
    mediaFiles = createListOfItems(mediaExt)
    
    soundsExt = ['.3gp', '.aa', '.aac', '.aax', '.act.dct', '.flac', '.m4a', '.m4b', '.m4p', '.mp3', '.mmf', '.msv', '.raw', '.sin', '.cda', '.amr', '.awb', '.ivs', '.nmf']
    soundFiles = createListOfItems(soundsExt)
    
    webExt = ['.html', '.css', '.js', '.json', '.php', '.django']
    webFiles = createListOfItems(webExt)
    
    iconsExt = ['.ico', '.svg']
    iconsFiles = createListOfItems(iconsExt)
    
    python = ['.py']
    pythonFiles = createListOfItems(python)
    
    exe = ['.exe']
    exeFiles = createListOfItems(exe)
    
    # extentions = [docExt, txtExt, pdfExt, imageExt, compressesdExt]
    # print(extentions)
    otherFiles = []
    ext = os.path.splitext
    for File in files:
        ext = os.path.splitext(File)[1].lower()
        if ext not in docExt and ext not in txtExt and ext not in imageExt and ext not in compressesdExt and ext not in pdfExt and os.path.isfile(File) and ext not in webExt and ext not in mediaExt and ext not in excelExt and ext not in accessExt and ext not in python and ext not in oneNoteExt and ext not in powerPointExt and ext not in soundsExt and ext not in iconsExt and ext not in exe:
            otherFiles.append(File)
    #    if ext not in docExt
    # # print(others)i
    print("Replacing...")
    automateFolderCreate("Docs", docFiles, "Document")
    automateFolderCreate("PDF", pdfFiles, "PDF")
    automateFolderCreate("Notepad Texts", txtFiles, "Text")
    automateFolderCreate("Images", imageFiles, "Image(s) or GIF")
    automateFolderCreate("Compressesd Files", compressesdFiles, "Compressed File(s)")
    automateFolderCreate("Media", mediaFiles, "Videos")
    automateFolderCreate("Sounds", soundFiles, "sounds or recordings")
    automateFolderCreate("Website Codes", webFiles, "Html or Js or Css or Php and other web languages")
    automateFolderCreate("Python Codes", pythonFiles, "Python codes")
    automateFolderCreate("Excel Sheets", excelFiles, "Excel")
    automateFolderCreate("Powerpoint Presentetions", powerPointFiles, "Powerpoint")
    automateFolderCreate("Access Databases", accessFiles, "Access database")
    automateFolderCreate("OneNotes", oneNoteFiles, "One Note(s)")
    automateFolderCreate("Icons", iconsFiles, ".ico & .svg Icon(s)")
    automateFolderCreate("Program Exe Files", exeFiles, ".exe Software(s)")
    automateFolderCreate("Others", otherFiles, "Other(s)")
    print("All files arranged successfully. Thanks for using this program.")
    a = input("Hit Enter to exit ")