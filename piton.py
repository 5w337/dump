import os
print(r"""
    ____                        _   _ _______________   
   / __ \ _____      _____  ___| |_/ |___ /___ /___  |  
  / / _` / __\ \ /\ / / _ \/ _ \ __| | |_ \ |_ \  / /   
 | | (_| \__ \\ V  V /  __/  __/ |_| |___) |__) |/ /    
  \ \__,_|___/ \_/\_/ \___|\___|\__|_|____/____//_/     
   \____/                                              
""")
def file_manager():
    while True:
        print("\nBasic file manager")
        print("1. list contents")
        print("2. create new directory")
        print("3. remove directory")
        print("4. create file")
        print("5. remove file")
        print("6. quit")
        try:
            secim=int(input("enter number: "))
        except ValueError:
            print("invalid number")
        if secim == 1:
            print("\n--- current directory contents ---")
            for file in os.listdir():
                if os.path.isfile(file):
                    print(f"files: {file}")
                elif os.path.isdir(file):
                    print(f"directories: {file}")
        elif secim== 2:
            newdir=input("enter new directory name: ")
            try:
                os.mkdir(newdir)
                print(f"{newdir} created sucessfuly")
            except FileExistsError:
                print("this directory name is already taken.")
        elif secim== 3:
            removedir = input("enter the directory you want to remove: ")
            try:
                os.rmdir(removedir)
                print("destroyed successfully")
            except FileNotFoundError:
                print("directory cannot be found")
            except PermissionError:
                print("Permission denied")
            except OSError as f:
                print("error deleting directory")
        elif secim==4:
            try:
                newfile=input("enter new file name: ")
                extension= input("enter file extension (e.g, .py, .exe, .txt): ")
                with open(newfile+extension, "x") as f:
                    print("created new file successfully")
            except FileExistsError:
                print(f"{newfile} name is already taken")
        elif secim==5:
            remove_file_name=input("enter the file you want to remove: ")
            try:
                os.remove(remove_file_name)
                print(f"{remove_file_name} destroyed successfully")
            except:
                print(f"{remove_file_name} cannot be found")
        elif secim == 6:
            print("shut down...")
            break
        else:
            print("invalid selection!")
file_manager()