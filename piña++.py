import os

# Preimports
login = 0

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
           \x1b[0;36mVersion: 0.1
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

p_exit         - Exit the program
p_clear        - Clear the console
p_ep           - Print a text in console
p_CFILE        - Create a file
p_WFILE        - Write a file
p_DELFILE      - Delete a file
p_RFILE        - Read a file
p_import:      - Import a module
p_use:         - Use a module
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
    if pcpp == "p_import:login":
        login = 1
        print("Imported sucessfull login!")
    if pcpp == "p_use:login":
        if login == 1:
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