print('''
      Author: Fahad
      Github : https://github.com/RF-Fahad-Islam/
      Thanks for using this program
      ''')
import os
from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askdirectory
# Function Global Variables
files = []
typeofFileList = []
value = ""
i = 0


def appendToInfoBox(text):
    global infoBox
    infoBox.insert(END, f"  {text}")


def appendToFlBox(text):
    global flBox
    flBox.insert(END, f"  {text}")

#!File Manager Functions


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
    global typeofFileList
    typeofFileList.append(typeofFile)
    if len(fileList) != 0:
        createFolder(folderName)
        replaceFile(folderName, fileList)
        print(f"\nGrouping : {fileList} as {typeofFile}")
        appendToInfoBox(f"\nGrouping : {typeofFile} files")
        appendToFlBox(f"***Replaced to {folderName} Folder***")
        appendToFlBox(f"- Type of file is {typeofFile}")
        appendToFlBox(
            f"- {folderName} folder containes {len(fileList)} file(s)")
        for File in fileList:
            appendToFlBox(f"- {File}")
        print(
            f"*** Successfully! {len(fileList)} {typeofFile} files replaced to {folderName} Folder ***")
        appendToInfoBox(
            f"*** Successfully! {len(fileList)} {typeofFile} files replaced to {folderName} Folder ***")


def about():
    tmsg.showinfo("About", "This is created by Fahad. #CodeWithHarry")

#!Main Folder Cleaner Function
def startProgram():
    global files
    infoBox.delete(1, END)
    print("Proccessing...")
    appendToInfoBox(f"Processing...")
    print(f"Total {len(files)} files on this directory")
    appendToInfoBox(f"Total {len(files)} files on this directory")
    if len(files) == 0:
        print("There are no files to arrange. All files already arranged.\nRun this program on another directory")
        appendToInfoBox("There are no files to arrange.")
        appendToInfoBox("All files already arranged.\n")
        appendToInfoBox("Run this program on another directory")
        a = input("Hit Enter to exit ")
        exit()

    print("Checking file types...")
    appendToInfoBox("Checking file types...")
    docExt = ['.doc', '.docx', 'docb', '.dotm', '.dot', '.xml', '.xps']
    docFiles = createListOfItems(docExt)

    powerPointExt = ['.pptx', '.pptm', '.potx', '.potm', '.ppam',
                     '.ppsx', '.ppsm', '.sldx', '.sldm', '.ppt', '.pot', '.pps']
    powerPointFiles = createListOfItems(powerPointExt)

    oneNoteExt = ['one']
    oneNoteFiles = createListOfItems(oneNoteExt)

    excelExt = ['.xls', '.xlt', '.xlm', '.xlsx', '.xlsm', '.xltx',
                '.xltm', '.xlsb', '.xla', '.xlam', '.xll', '.xlw']
    excelFiles = createListOfItems(excelExt)

    accessExt = ['.accdb', '.accde', '.accdt', '.accdr']
    accessFiles = createListOfItems(accessExt)

    txtExt = ['.txt']
    txtFiles = createListOfItems(txtExt)

    imageExt = ['.jpg', '.jpeg', '.png',
                '.gif', '.tif', '.tiff', '.eps', '.row']
    imageFiles = createListOfItems(imageExt)

    pdfExt = ['.pdf']
    pdfFiles = createListOfItems(pdfExt)

    compressesdExt = ['.zip', '.rar', '.z',
                      '.arj', '.deb', '.pkg', '.rpm', 'z', '.7z']
    compressesdFiles = createListOfItems(compressesdExt)

    mediaExt = ['.webm', '.mpg', '.mp2', '.mpeg', '.mpe', '.mpv',
                '.ogg', '.mp4', '.mov', '.qt', '.flv', '.swf', '.avchd']
    mediaFiles = createListOfItems(mediaExt)

    soundsExt = ['.3gp', '.aa', '.aac', '.aax', '.act.dct', '.flac', '.m4a', '.m4b', '.m4p',
                 '.mp3', '.mmf', '.msv', '.raw', '.sin', '.cda', '.amr', '.awb', '.ivs', '.nmf']
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
    print("Replacing...")
    appendToInfoBox("Replacing...")
    automateFolderCreate("Docs", docFiles, "Document")
    automateFolderCreate("PDF", pdfFiles, "PDF")
    automateFolderCreate("Notepad Texts", txtFiles, "Text")
    automateFolderCreate("Images", imageFiles, "Image(s) or GIF")
    automateFolderCreate("Compressesd Files",
                         compressesdFiles, "Compressed File(s)")
    automateFolderCreate("Media", mediaFiles, "Videos")
    automateFolderCreate("Sounds", soundFiles, "sounds")
    automateFolderCreate("Website Codes", webFiles,
                         "Html or Js or Css or Php and other web languages")
    automateFolderCreate("Python Codes", pythonFiles, "Python codes")
    automateFolderCreate("Excel Sheets", excelFiles, "Excel")
    automateFolderCreate("Powerpoint Presentetions",
                         powerPointFiles, "Powerpoint")
    automateFolderCreate("Access Databases", accessFiles, "Access database")
    automateFolderCreate("OneNotes", oneNoteFiles, "One Note(s)")
    automateFolderCreate("Icons", iconsFiles, ".ico & .svg Icon(s)")
    automateFolderCreate("Program Exe Files", exeFiles, ".exe Software(s)")
    automateFolderCreate("Others", otherFiles, "Other(s)")
    print("All files arranged successfully. Thanks for using this program.")
    appendToInfoBox("All files arranged successfully.")
    remove_all()
    tmsg.showinfo("Proccessing Finished!",
                  "All Selected Files Arranged SuccessFully!")
    files = []
    update_list()
    appendToInfoBox("Thanks For using this program")
    # a = input("Hit Enter to exit ")
    # update_list()

#!Tkinter GUI Functions


def update_list():
    global files
    global status
    # Assign New Directory Files
    files = os.listdir()
    remove_files_list = ["folder_cleaner_GUI.py", "icon.ico"]
    for File in remove_files_list:
        if File in files:
            files.remove(File)

    files = [File for File in files if os.path.isfile(File)]
    status.set(f"{os.getcwd()} (Current Directory)")
    statusbar.update()
    # listbox.insert(END, "Files List----")
    get_len()
    if len(files) == 0:
        tmsg.showwarning("No Unfolder file found!",
                         f"No unfolder files found on \"{os.getcwd()}\" directory")
        # listbox.insert(END, " No unfolder files on this directory")
    else:
        for File in files:
            listbox.insert(END, f" -  {File}")


def setDirectory():
    global files
    directory = askdirectory()
    if directory == "":
        pass
    else:
        os.chdir(directory)
        listbox.delete(1, END)
        infoBox.delete(1, END)
        get_len()
        update_list()


def remove_item():
    global files
    global listbox
    global value
    sel = listbox.curselection()
    values = []
    for s in sel:
        value = listbox.get(s)
        value = value[4:]
        values.append(value)

    for index in sel[::-1]:
        listbox.delete(index)

    for v in values:
        if value in files:
            files.remove(v)
    print(files)
    print(f"The value is {values}")
    print(sel)
    print(f"The index is {sel[::-1]}")


def get_len():
    lenList = len(files)
    infoBox.delete(1)
    infoBox.insert(END, f" There are {lenList} Unfolder File(s)")


def remove_all():
    listbox.delete(1, END)


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x700")
    root.minsize(600, 650)
    root.title("Automatic File Manager")
    root.wm_iconbitmap("folder.ico")
    # Mainmenu
    mainmenu = Menu(root)
    filemenu = Menu(mainmenu, tearoff=0)
    filemenu.add_command(label="Change Directory", command=setDirectory)
    mainmenu.add_cascade(label="File", menu=filemenu)

    toolmenu = Menu(mainmenu, tearoff=0)
    toolmenu.add_command(label="Remove", command=remove_item)
    toolmenu.add_command(label="Remove All", command=remove_all)
    mainmenu.add_cascade(label="Tools", menu=toolmenu)

    helpmenu = Menu(mainmenu, tearoff=0)
    helpmenu.add_command(label="About", command=about)
    mainmenu.add_cascade(label="Help", menu=helpmenu)
    mainmenu.add_command(label="Run", command=startProgram)
    root.config(menu=mainmenu)
    # Heading
    header = StringVar()
    header.set(f"Arrange Your Files Automatically - Created By Fahad")
    header = Label(root, textvariable=header, font="helvatica 12 bold",
                   padx=10, pady=5, anchor="w", relief=SUNKEN)
    header.pack(fill=X, side=TOP, pady=5, padx=5)
    # Listbox
    listboxSbY = Scrollbar(root)
    # listboxSbX = Scrollbar(root)
    listboxSbY.pack(fill=Y, side=RIGHT)
    # listboxSbX.pack(fill=X, side=TOP)
    listbox = Listbox(root, font="Helvatica 12 bold",
                      yscrollcommand=listboxSbY.set, selectmode=EXTENDED)
    listbox.pack(fill=X, pady=3, padx=30)
    listbox.insert(END, "The Directory UnFolder Files List")
    listboxSbY.config(command=listbox.yview)
    # listboxSbX.config(command=listbox.xview)
    # Command status showing Box
    infoBox = Listbox(root, font="Helvatica 10 bold",
                      height=8, selectmode=SINGLE)
    infoBox.pack(pady=3, padx=30, side=TOP, fill=X)
    infoBox.insert(END, "The Status of Commands")
    # Command status showing Box
    lenlist = listbox.size()
    flBox = Listbox(root, font="Helvatica 10 bold",
                    width=50, height=15, selectmode=SINGLE)
    flBox.pack(pady=3, padx=30, side=RIGHT)
    flBox.insert(END, "The Files Status")
    # Frames
    f1 = Frame(root)
    f2 = Frame(root)
    f3 = Frame(root)
    f4 = Frame(root)
    # Button
    b = Button(root, text="Change Directory", font="Helvatica 10 bold",
               padx=3, pady=3, command=setDirectory)
    b.pack(padx=10, pady=10, fill=X)
    b = Button(root, text="Run", font="comicsans 10 bold", bg="green",
               fg="white", padx=3, pady=3, command=startProgram)
    b.pack(pady=10, padx=20, fill=X)
    b = Button(root, text="Remove", font="comicsans 10 bold",
               padx=3, pady=3, bg="lightGrey", command=remove_item)
    b.pack(pady=10, padx=10, fill=X)
    b = Button(root, text="Remove All", font="comicsans 10 bold",
               padx=3, pady=3, bg="red", fg="white", command=remove_all)
    b.pack(pady=10, padx=10, fill=X)
    f1.pack()
    f2.pack()
    # StatusBar
    status = StringVar()
    status.set(f"{os.getcwd()} (Current Directory)")
    statusbar = Label(f4, textvariable=status, font="Helvatica 8 bold",
                      bg="white", padx=6, pady=10, anchor="w", relief=GROOVE, borderwidth=3)
    statusbar.pack(fill=X, side=BOTTOM, anchor="s", expand=True, pady=10)
    f4.pack(side="bottom", anchor="s")
    if i < 1:
        update_list()
        get_len()
    i += 1
    root.mainloop()
