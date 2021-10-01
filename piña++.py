import os

# Preimports
importlogin = 0
importroot = 0

print("\x1b[0;35m")

print("""
  ____  _  /\/|                   
 |  _ \(_)|/\/   __ _   _     _   
 | |_) | | '_ \ / _` |_| |_ _| |_ 
 |  __/| | | | | (_| |_   _|_   _|
 |_|   |_|_| |_|\__,_| |_|   |_|  

\x1b[0;31m
###################################
             \x1b[0;34mBy x04000
     \x1b[0;33mGithub: github.com/x04000
           \x1b[0;32mBase: Python
           \x1b[0;36mVersion: 0.2
\x1b[0;31m###################################
\x1b[0;35m
""")
while(True):
    pcpp = str(input("Piña++ > "))
    print("")
    if pcpp == "p_help":
        print("""
\x1b[0;31m    
  /\  /\___| |_ __  
 / /_/ / _ \ | '_ \ 
/ __  /  __/ | |_) |
\/ /_/ \___|_| .__/ 
             |_|    
\x1b[0;35m

p_exit                 - Exit the program
p_clear                - Clear the console
p_ep                   - Print a text in console
p_CFILE                - Create a file
p_WFILE                - Write a file
p_DELFILE              - Delete a file
p_RFILE                - Read a file
p_import:              - Import a module
p_use:                 - Use a module
p_packages             - View piña++packages
p_rmpackage-PACKAGE    - Remove a piña++ package
p_gitclone             - Use Git clone
p_pip                  - Use pip fuctions
p_systemterminal       - To use your terminal commands
p_python               - Use the python terminal
p_python3              - Use the python3 terminal
        """)
    if pcpp == "p_exit":
        exit()
    if pcpp == "p_clear":
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()
    if pcpp == "p_ep":
        ep = str(input("Piña++ EP > "))
        print("")
        print(ep)
        print("")
    if pcpp == "p_CFILE":
        file = str(input("Piña++ CFILE > "))
        f=open(file,"w")
        f.close()
    if pcpp == "p_WFILE":
        file = str(input("Piña++ FILENAME > "))
        write = str(input("Piña++ WRITE > "))
        f=open(file, "w")
        f.write(write)
        f.close()
    if pcpp == "p_DELFILE":
        file = str(input("Piña++ FILENAME > "))
        delfilewin = "del /f /a "+file
        delfilelinux = "rm "+file
        os.system(delfilewin if os.name in ('nt', 'dos') else delfilelinux)
    if pcpp == "p_RFILE":
        file = str(input("Piña++ FILENAME > "))
        try:
            with open(file,"r") as archivo:
                for linea in archivo:
                    print(linea)
        except:
            print("File can't load!")
    if pcpp == "p_packages":
        print("")
        print("[Piña++ Package List]")
        print("")
        print("Installed")
        if importlogin == 1:
            print("login")
        if importroot == 1:
            print("root")
        if importlogin == 0:
            print("login")
        if importroot == 0:
                print("root")
    if pcpp == "p_rmpackage-login":
        print("")
        if importlogin == 1:
            print("Are you sure? [Y/N]")
            sure = str(input("Piña++ OPTION > "))
            if sure == "Y" or "y":
                importlogin = 0
                print("Package login has been removed!")
            if sure == "N" or "n":
                print("Package login hasn't been removed!")
            else:
                print("Invalid option!")
        else:
            print("Package is not installed!")
    if pcpp == "p_rmpackage-root":
        print("")
        if importlogin == 1:
            print("Are you sure? [Y/N]")
            sure = str(input("Piña++ OPTION > "))
            if sure == "Y" or "y":
                importroot = 0
                print("Package login has been removed!")
            if sure == "N" or "n":
                print("Package login hasn't been removed!")
            else:
                print("Invalid option!")
        else:
            print("Package is not installed!")
    if pcpp == "p_import:login":
        importlogin = 1
        print("Imported sucessfull login!")
    if pcpp == "p_use:login":
        if importlogin == 1:
            from getpass import getpass
            parameter = str(input("Piña++ DEFINE:PARAMETER (Optional) > "))
            user = str(input("Piña++ DEFINE:USER > "))
            password = getpass("Piña++ DEFINE:PASSWORD > ")
            print("")
            useri = str(input("Username: "))
            if useri == user:
                passwordi = getpass("Password: ")
                if str(passwordi) == password:
                    print("Sucesfull login!")
                    print("")
                    if parameter == "debugmode":
                        print("""
#####################
        DEBUG  
#####################
                        """)
                        print("Username="+useri)
                        print("Password="+passwordi)
                        break
                    else:
                        print("Incorrect password!")
                else:
                    print("Incorrect username!")
        else:
            print("No module found called: login! You can import them with P_import:MODULENAME")
    if pcpp == "p_import:root":
        importroot = 1
        root = 0
        print("Imported sucessfull root!")
    if pcpp == "p_use:root":
        if importroot == 1:
            from getpass import getpass
            try:
                if root == 0:
                    if rootpassword == "":
                        """ CHECK """
                    print("")
                    while(True):
                        rootpasswordi = getpass("Piña++ RootPassword > ")
                        if rootpasswordi == rootpassword:
                            root = 1
                            print("Sucessfull login as root!")
                            break
                        else:
                            print("Invalid password!")
                else:
                    root=  0
                    print("")
                    print("Sucessfull login as home!")
            except:
                print("No root password set!")
        else:
            print("No module found called: root! You can import them with P_import:MODULENAME")
    if pcpp == "p_use:root-set":
        if importroot == 1:
            from getpass import getpass
            rootpassword = getpass("Piña++ DEFINE:RootPassword > ")
            print("")
            print("Password set!")
        else:
            print("No module found called: root! You can import them with P_import:MODULENAME")
    if pcpp == "p_use:root-check":
        if importroot == 1:
            if root == 1:
                print("You are root!")
            else:
                print("You aren't root!")
    if pcpp == "p_gitclone":
        gitcloneurl = str(input("URL of Git > "))
        gitclonecommand = "git clone "+gitcloneurl
        try:
            os.system(gitclonecommand)
        except:
            print("Git error!")
    if pcpp == "p_ls":
        os.system("dir" if os.name in ('nt', 'dos') else "ls")
        print("")
    if pcpp == "p_pip":
        print("""[Piña++ Pip Help]

p_pip-install     - Install a package with pip
p_pip-uninstall   - Uninstall a package with pip
p_pip-list        - Show the pip list
        """)
    if pcpp == "p_pip-install":
        pipinstallpackage = str(input("Name of package > "))
        pipinstallcommand = "pip install "+pipinstallpackage
        try:
            os.system(pipinstallcommand)
        except:
            print("Python: Pip error!")
    if pcpp == "p_pip-uninstall":
        pipuninstallpackage = str(input("Name of package > "))
        pipuninstallcommand = "pip uninstall "+pipuninstallpackage
        try:
            os.system(pipuninstallcommand)
        except:
            print("Python: Pip error!")
    if pcpp == "p_pip-list":
        try:
            os.system("pip list")
        except:
            print("Python: Pip error!")
    if pcpp == "p_ruso":
        print("VOZKAAAAA")
        try:
            f=open("vozka.txt","w")
            f.write("VIVA ER VOZKAAAAAA")
            f.close()
        except:
            print("VOSKA ERROR :)")
    if pcpp == "p_systemterminal":
        print("[Piña++ System Terminal]")
        print("")
        print("""[INFO]

You can use your terminal commands here ;)
To close the System Terminal use: p_closeterminal

        """)
        while(True):
            systemterminalcommand = str(input("Piña++ SysTerminal > "))
            print("")
            if systemterminalcommand == "p_closeterminal":
                break
            else:
                try:
                    os.system(systemterminalcommand)
                except:
                    print("Piña++ System Terminal error!")
    if pcpp == "p_python":
        print("[Piña++ Python]")
        print("")
        try:
            os.system("python")
        except:
            print("Piña++ can't load python. Revise your python installation")
    if pcpp == "p_python3":
        print("[Piña++ Python3]")
        print("")
        try:
            os.system("python3")
        except:
            print("Piña++ can't load python3. Revise your python3 installation")