#!/usr/bin/python

import os
import re
import sys
import requests

logo='''\033[1;92m
  ______      __             _       __
 /_  __/_  __/ /_____  _____(_)___ _/ /
  / / / / / / __/ __ \/ ___/ / __ `/ /
 / / / /_/ / /_/ /_/ / /  / / /_/ / /
/_/  \__,_/\__/\____/_/  /_/\__,_/_/
\n\033[1;97mSilahkan Anda Ketik No 1 Untuk Menginstall 
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
print (logo)