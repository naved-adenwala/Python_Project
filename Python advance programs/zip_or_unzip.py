
import os
import zipfile
try:
    path = input("Enter directory path ")
    os.chdir(path)
    ask = input("You want to zip or unzip the files ").lower()
    if ask == "zip":
        count = 1
        file_name = input("Give name to your zip files ") + ".zip"
        n = int(input("How many files you want to zip "))
        name = zipfile.ZipFile(file_name,"w")
        for k in range(1,n+1):
            writ = input("Enter file names one by one :")
            name.write(writ,compress_type=zipfile.ZIP_DEFLATED)
            print(count,"File is added successfully")
            count +=1
        name.close()
except FileNotFoundError as f:
    print("Error Please Enter Correct file name")

except ValueError as v:
    print("Error Please Enter only number")

else:
    print(os.getcwd())
    un_file = input("zip file name to extract all ")
    z = zipfile.ZipFile(un_file,"r")
    z.extractall()
    z.close()


