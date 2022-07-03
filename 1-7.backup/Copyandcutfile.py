import shutil, os

# shutil.move(r"C:\Users\Phat Diep\Desktop\Summer 22\python summer 22\28-6-regular-expression.py",\
#     r"C:\Users\Phat Diep\Desktop\Summer 22\python summer 22\1-7")

path = r"C:\Users\Phat Diep\Desktop\Summer 22\python summer 22"

for Foldername,Subfolders,filenames in os.walk(path):
    print("Folder cha tên là "+Foldername)
    print("Các folder con nằm trong folder cha "+Foldername+ " là "+str(Subfolders))
    print("Các file name nằm trong folder cha "+Foldername+"là"+str(filenames))
    print()
    # for subfolder in Subfolders:
        # if subfolder == "Vcl":
        #     os.rmdir(os.path.join(path,subfolder))
        #     for file in filenames:
    for file in filenames:
        if file.endswith(".py"):
            folderbk=os.path.basename(Foldername)
            if not os.path.isdir(os.path.join(Foldername,folderbk + ".backup")):
                os.mkdir(os.path.join(Foldername,folderbk+".backup"))
            shutil.copy(os.path.join(Foldername,file),os.path.join(Foldername,folderbk+".backup"))


