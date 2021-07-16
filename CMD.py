#!/usr/bin/python

import os
import re
import sys
import requests

def bahan():
	os.system('clear')
	print (logo2)
	os.system('pkg update')
	os.system('pkg upgrade')
	os.system('pkg install python')
	os.system('pkg install python2')
	os.system('pkg install python3')
	os.system('pkg install git')
	os.system('pkg install php')
	os.system('pip2 install requests')
	os.system('pip install requests')
	os.system('pip2 install mechanize')
	os.system('pip install mechanize')
	os.system('pip2 install bs4')
	os.system('pip install bs4')
	os.system('pip2 install nodejs')
	os.system('pip install nodejs')
	os.system('apt update && apt upgrade')
	os.system('pip install --upgrade pip')
	print (logo3)
	exit()

logo='''
\033[1;95m
        _          _
         \        /
        __\______/__
        | [©]  [©] |​
        |  [====]  |
\033[1;93m    ╔══\033[1;95mo00\033[1;93m════════\033[1;95m00o\033[1;93m═════════════════════════════╗
\033[1;94m    █ \033[1;97m  [01] Install Perintah Termux              \033[1;94m█
\033[1;94m    █\033[1;97m   [02] Cara Menggunakan Tools Ini           \033[1;94m█
\033[1;94m    █\033[1;97m   [00] Keluar                               \033[1;94m█
\033[1;93m    ╚═════════════════════════════════════════════╝

\033[1;97mCoding By : Pahrul

'''

logo2=('''\033[1;92m
  ______                                 
 /_  __/_  ______  ____ _____ ___  __    
  / / / / / / __ \/ __ `/ __ `/ / / /    
 / / / /_/ / / / / /_/ / /_/ / /_/ / _ _ 
/_/  \__,_/_/ /_/\__, /\__, /\__,_(_|_|_)
                /____//____/             \033[1;97m
''')

logo3=('''\033[1;92m
  _____      __                _    
  / ___/___  / /__  _________ _(_)   
  \__ \/ _ \/ / _ \/ ___/ __ `/ /    
 ___/ /  __/ /  __(__  ) /_/ / / _ _ 
/____/\___/_/\___/____/\__,_/_(_|_|_)\033[1;97m''')
                              
def menu():
	os.system("clear")
	print(logo)
	pilih()
	

def pilih():
	print("\033[1;97m╭───[ \033[1;97mPilih Menu\033[1;97m ]")
	p = input("\033[1;97m╰───⟩⟩⟩\033[1;97m\033[1;92m ")
	if p=='1':
		bahan()
	if p=='2':
		os.system('python tutor.py')
		exit()
	elif p=='0':
		print("\n\033[1;97mTerimakasih Telah Menggunakan Tool Saya !!!")
		os.sys.exit()
	else:
		print("\n\033[1;97mPilihan Tidak Di Ketahui !!!m")
		os.sys.exit()
		
if __name__ == '__main__':
	menu()