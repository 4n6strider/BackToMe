# BackToMe
<img src="https://img.shields.io/badge/Python-2.7.13-blue.svg"> <img src="https://img.shields.io/badge/OS-Win%20Lin%20Osx-green.svg"> <img src="https://img.shields.io/badge/phase-development-orange.svg"> <img src="https://img.shields.io/badge/verssion-1.0--unstable-red.svg"><br>
Little framework made in python to create payloads for Linux, Windows and OSX with unique handler.

# INFOS
This little framework is intended to help pentesters/red teamers in creating FUD payloads with unique handler-listener

# COMMANDS
- <b>getinfos</b> | Get system infos. Ex: User,Kernel, OS,Architecture
- <b>getpartitions</b> | Get sysem partitions and type. Ex: "/dev/sda1" "ext4"
- <b>newtwork</b> | Get newtork infos about network. Ex: ifconfig (Linux&Osx) ipconfig (Windows)
- <b>windows-rdp</b> | Try to enable RDP and creare a new user for it (Need admin privileges!)
- <b>enumerate-win</b> | Get windows based os infos. Ex: some net actions and some info gathering actions
- <b>enumerate-linux</b> | Get linux based os infos. Ex: ssh root acces enabled and some info gathering actions
- <b>drop into terminal</b> | Try to get bash/cmd session with sockets.
