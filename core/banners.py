#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from termcolor import colored
import random
author = colored('H0nus','red',attrs=['bold'])
email= colored('h0nus-apt[at]protonmail[dot]com','yellow',attrs=['bold'])
version = colored('v1.0','white')


banner1 = """
_________________________________________________________
    ____                      ______         _   _
    /   )                /      /            /  /|  {}
---/__ /-----__----__---/-__---/-------__---/| /-|----__-
  /    )   /   ) /   ' /(     /      /   ) / |/  |  /___)
_/____/___(___(_(___ _/___\__/______(___/_/__/___|_(___ _

\t\b\b\b\b{} ~ {}""".format(version,author,email)

banner2 ="""
\t╔╗ ┌─┐┌─┐┬┌─╔╦╗┌─┐╔╦╗┌─┐
\t╠╩╗├─┤│  ├┴┐ ║ │ │║║║├┤
\t╚═╝┴ ┴└─┘┴ ┴ ╩ └─┘╩ ╩└─┘
                        {}
\t\b\b\b\b\b{} ~ {}
""".format(version,author,email)

banner3="""
██████╗  █████╗  ██████╗██╗  ██╗████████╗ ██████╗ ███╗   ███╗███████╗
██╔══██╗██╔══██╗██╔════╝██║ ██╔╝╚══██╔══╝██╔═══██╗████╗ ████║██╔════╝
██████╔╝███████║██║     █████╔╝    ██║   ██║   ██║██╔████╔██║█████╗
██╔══██╗██╔══██║██║     ██╔═██╗    ██║   ██║   ██║██║╚██╔╝██║██╔══╝
██████╔╝██║  ██║╚██████╗██║  ██╗   ██║   ╚██████╔╝██║ ╚═╝ ██║███████╗
╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚══════╝
                                                    {}
\t{} ~ {}
""".format(version,author,email)

def get_banner():
    banners = [banner1, banner2, banner3]
    return random.choice(banners)
