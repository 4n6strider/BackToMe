#!/bin/bash
echo "_________________________________________________________"
echo "    ____                      ______         _   _       "
echo "    /   )                /      /            /  /|  v1.0 "
echo "---/__ /-----__----__---/-__---/-------__---/| /-|----__-"
echo "  /    )   /   ) /   ' /(     /      /   ) / |/  |  /___)"
echo "_/____/___(___(_(___ _/___\__/______(___/_/__/___|_(___ _"
echo ""
echo "                BackToMe full installer"
echo "        by H0nus h0nus-apt[at]protonmail[dot]com"
sleep 2
if [ $EUID != 0 ]
  then
  echo "You need to run this as root!"
  exit 1
fi
echo "Updating repositories"
sudo apt-get update
if ! hash wine 2>/dev/null
  then
  echo "Installing Wine"
  sudo apt-get install wine -y
  echo "Done"
  sleep 1
else
  echo "Wine is installed"
  sleep 1
fi
if ! hash pip 2>/dev/null
  then
  echo "Installing Pip"
  sudo apt-get install python-pip -y
  echo "Done"
  sleep 1
else
  echo "Pip is installed"
  sleep 1
fi
if ! hash pyinstaller 2>/dev/null
  then
  echo "Installing PyInstaller"
  sudo pip install pyinstaller
  echo "Done"
  sleep 1
else
  echo "PyInstaller is installed"
  sleep 1
fi

if [ `getconf LONG_BIT` = "64" ]
  then
  wget https://www.python.org/ftp/python/2.7/python-2.7.amd64.msi
  sudo wine msiexec /i python-2.7.amd64.msi
else
  wget https://www.python.org/ftp/python/2.7/python-2.7.msi
  sudo wine msiexec /i python-2.7.msi
fi
sudo mv configs/get_pip.py /root/.wine/drive_c/Python2.7/
cd /root/.wine/drive_c/Python2.7/ && sudo wine python get_pip.py
sudo pip install -r requirements.txt
