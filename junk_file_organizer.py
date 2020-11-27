import os 
import shutil
import random
import time
import datetime

print("Welcome To Junk File Organizer")
print("Project developed by Ayyappan")
print("Choose your option: ")
print("-------------------------------------------")
print("1 : Orginaze by File Extension")
print("2 : Organize by File Size")
print("3 : Organize by File Date")
print("-------------------------------------------")
typeofsort = input("Enter Organize Method Option: ")
folderpath = input('Enter any Directory path to Sort the Files: ')

# To Sort According To Extensions
class JunkFileOrganiser:
    def __init__(self):
        self.file_extentions = dict
        self.new_path = "organized"
file_extensions={

    "Audio_Files" : (".aif", ".cda", ".mid", ".mp3", ".mpa", ".ogg", ".wav", ".wpl"),
    
    "ASP_Files" : (".asp", ".aspx"),
    
    "Compressed_Files" : (".7z", ".arj", ".deb", ".pkg", ".rar", ".rpm", ".tar", ".gz", ".z", ".zip"),
    
    "CSS_Files" : (".css"),

    "Disc_and_Media_Files" : (".bin", ".dmg", ".iso", ".toast", ".vcd"),
    
    "Database_Files" : (".csv", ".dat", ".db", ".dbf", ".log", ".mdb", ".sav", ".sql", ".tar", ".xml"),
    
    "Email_Files" : (".email", ".eml", ".emlx", ".msg", ".oft", ".ost", ".pst", ".vcf"),
    
    "Executable_Files" : (".apk", ".bat", ".bin", ".cgi", ".pl", ".com", ".exe", ".gadget", ".jar", ".msi", ".wsf"),
    
    "Fonts" : (".fnt", ".font", ".otf", ".ttf"),
    
    "HTML_Files" : (".htm", ".html", ".xhtml", ".html5"),

    "Images" : (".ai", ".bmp", ".gif", ".ico", ".jpeg", ".jpg", ".png", ".ps", ".psd", ".svg", ".tiff", ".tif"),
    
    "Internet_related_Files" : (".cer", ".cfm", ".cgi", ".pl", ".js", ".jsp", ".part", ".rss"),
    
    "PDF_Files" : (".pdf"),

    "PHP_Files" : (".php"),

    "Presentation_Files" : (".key", ".odp", ".pps", ".ppt", ".pptx"),

    "Programming_Files" : (".c", ".class", ".cpp", ".cs", ".h", ".java", ".sh", ".swift", ".vb"),

    "Python_Files" : (".py"),

    "Spreadsheets" : (".ods", ".xls", ".xlsm", ".xlsx"),

    "System_Files" : (".bak", ".cab", ".cfg", ".cpl", ".cur", ".dll", ".dmp", ".drv", ".icns", ".ini", ".lnk", ".msi", ".sys", ".tmp"),

    "Text_Files" : (".rtf", ".tex", ".txt"),

    "Videos" : (".3g2", ".3gp", ".avi", ".flv", ".h264", ".m4v", ".mkv", ".mov", ".mp4", ".mpg", ".mpeg", ".rm", ".swf", ".vob", ".wmv"),

    "Word_Files" : (".doc", ".docx", ".odt", ".wpd")

    }
new_path={
    "Organized":("Audio_Files","ASP_Files","Compressed_Files","CSS_Files","Disc_and_Media_Files","Database_Files","Email_Files","Executable_Files","Fonts","HTML_Files","Images","Internet_related_Files","PDF_Files","PHP_Files","Presentation_Files","Programming_Files","Python_Files","Spreadsheets","System_Files","Text_Files","Videos","Word_Files")
}


if typeofsort=="1":
    print("File Organizing in progress by file extensions, Please wait...")
    wait_time = random.randint(1,30)
    time.sleep(wait_time)
    
    def file_finder(folderpath,file_extensions):
        files=[]
        for file in os.listdir(folderpath):
            for extension in file_extensions:
                if file.endswith(extension):
                    files.append(file)
        return files 

    for extensions_type,extension_tuple in file_extensions.items():
        folder_name=extensions_type.split('_')[0]
        folder_path=os.path.join(folderpath,folder_name)
        os.mkdir(folder_path)
        for item in (file_finder(folderpath,extension_tuple)):
            item_path=os.path.join(folderpath,item)
            item_new_path=os.path.join(folder_path,item)
            shutil.move(item_path,item_new_path)

    for extensions_type,extension_tuple in new_path.items():
        folder_name=extensions_type.split('_')[0]
        folder_path=os.path.join(folderpath,folder_name)
        os.mkdir(folder_path)
        for item in (file_finder(folderpath,extension_tuple)):
            item_path=os.path.join(folderpath,item)
            item_new_path=os.path.join(folder_path,item)
            shutil.move(item_path,item_new_path)
    print("File organizing completed by Extenstions.")


# To Organize the file by size

if typeofsort=="2":
    print("File Organizing in progress by size of files, Please wait...")
    wait_time = random.randint(1,30)
    time.sleep(wait_time)
    
    def sizecheck(folderpath):
        list_dir=os.walk(folderpath)
        for dir,filename, file in list_dir:
            for f in file:
                sizeoffile=os.stat(dir+"/"+f).st_size
                try:
                    if sizeoffile < 1024:
                        if os.path.exists(folderpath+"/Byte_Files/"):
                            shutil.move(folderpath+"/"+f, folderpath+"/Byte_Files/"+f)
                        else:
                            os.mkdir(folderpath+"/Byte_Files/")
                            shutil.move(folderpath+"/"+f, folderpath+"/Byte_Files/"+f)
                    elif sizeoffile >= 1024 and sizeoffile < 1000*1024:
                        if os.path.exists(folderpath+"/KiloBytes_Files/"):
                            shutil.move(folderpath+"/"+f, folderpath+"/KiloBytes_Files/"+f)
                        else:
                            os.mkdir(folderpath+"/KiloBytes_Files/")
                            shutil.move(folderpath+"/"+f, folderpath+"/KiloBytes_Files/"+f)
                    elif sizeoffile >= 1000*1024 and sizeoffile <= 1000*1024*1024:
                        if os.path.exists(folderpath+"/MegaBytes_Files/"):
                            shutil.move(folderpath+"/"+f, folderpath+"/MegaBytes_Files/"+f)
                        else:
                            os.mkdir(folderpath+"/MegaBytes_Files/")
                            shutil.move(folderpath+"/"+f, folderpath+"/MegaBytes_Files/"+f)
                    else:
                        if os.path.exists(folderpath+"/GigaBytes_Files/"):
                            shutil.move(folderpath+"/"+f, folderpath+"/GigaBytes_Files/"+f)
                        else:
                            os.mkdir(folderpath+"/GigaBytes_Files/")
                            shutil.move(folderpath+"/"+f, folderpath+"/GigaBytes_Files/"+f)
                except FileExistsError:
                    continue
        print("File organizing completed by Size.")

# To Organize the file by Date and Time
if typeofsort=="3":
    print("File Organizing in progress by date of files, Please wait...")
    wait_time = random.randint(1,30)
    time.sleep(wait_time)
    
    def date_sort(folderpath):
        list_dir=os.walk(folderpath)
        for dir,filename, file in list_dir:
            for f in file:
                dateoffile=os.stat(dir+"/"+f).st_size
                try:
                    if dateoffile < 1024:
                        if os.path.exists(folderpath+"/Less than 10 days/"):
                            shutil.move(folderpath+"/"+f, folderpath+"/Less than 10 days/"+f)
                        else:
                            os.mkdir(folderpath+"/Less than 10 days/")
                            shutil.move(folderpath+"/"+f, folderpath+"/Less than 10 days/"+f)
                    elif dateoffile >= 1024 and dateoffile < 1000*1024:
                        if os.path.exists(folderpath+"/Morethan 10 days to less than 20 days/"):
                            shutil.move(folderpath+"/"+f, folderpath+"/Morethan 10 days to less than 20 days/"+f)
                        else:
                            os.mkdir(folderpath+"/Morethan 20 days to less than 30 days/")
                            shutil.move(folderpath+"/"+f, folderpath+"/Morethan 20 days to less than 30 days/"+f)
                    elif dateoffile >= 1000*1024 and dateoffile <= 1000*1024*1024:
                        if os.path.exists(folderpath+"/A month ago/"):
                            shutil.move(folderpath+"/"+f, folderpath+"/A month ago/"+f)
                        else:
                            os.mkdir(folderpath+"/A month ago/")
                            shutil.move(folderpath+"/"+f, folderpath+"/A month ago/"+f)
                    else:
                        if os.path.exists(folderpath+"/More than a month/"):
                            shutil.move(folderpath+"/"+f, folderpath+"/More than a month/"+f)
                        else:
                            os.mkdir(folderpath+"/More than a month/")
                            shutil.move(folderpath+"/"+f, folderpath+"/More than a month/"+f)
                except FileExistsError:
                    continue
        print("File organizing completed by Date.")
    date_sort(folderpath)

if __name__ == '__main__':
    junkfile = JunkFileOrganiser()
