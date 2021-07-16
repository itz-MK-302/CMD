#!/usr/bin/python

import os
import re
import sys
import requests

logo='''\n\033[1;97mSilahkan Anda Ketik No 1 Untuk Menginstall 
Perintah Termux  Lalu Tunggu Hingga 
Proses Penginstallan Selesai...
Jika muncul pertanyaan Dan Di Suruh Jawab
Contoh Nya Seperti Ini
Do you want to continue? [Y/n]
Silahkan Kalian Ketik Y Lalu Enter
jika Kalian sudah menggunakan script ini tidak di 
wajibkan untuk menggunakannya lagi
\033[1;92m
Terimakasih :)
'''

os.system('clear')
print ('\033[1;92m')
os.system('figlet -f slant Tutorial')
print (logo)

