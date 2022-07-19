import os
import platform
import hashlib
import colorama
import time
import sys
from hashlib import *
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.001)
if platform.system() == 'Linux':
    os.system('clear')
if platform.system() == 'Windows':
    os.system('cls')
colorama.init(autoreset=True)
logo = '''\033[31m
                        ,     ,
                        |\---/|
                       /  , , |
                  __.-'|  / \ /
         __ ___.-'        ._O|
      .-'  '        :      _/
     / ,    .        .     |    \033[31m@hx7 CyBer Team
    :  ;    :        :   _/    \033[31m- Hashing Tools -
    |  |   .'     __:   /
    |  :   /'----'| \  |
    \  |\  |      | /| |
     '.'| /       || \ |
     | /|.'       '.l \\_
     || ||             '-'
     '-''-'
'''
typingPrint(logo)
typingPrint("=========================================================================\n")
typingPrint("\033[33m1]- Hash Checker\n2]- Hash Length Calculator\n3]- Hash Type Checker\n")
typingPrint("\033[33m4]- MD5 Encrypt\n5]- MD5 Decrypt \033[37m\n")
typingPrint("\n=========================================================================\n")
choose = input("Please Choose Option : ")
if choose == '1':
    if platform.system() == 'Linux':
        os.system('clear')
    if platform.system() == 'Windows':
        os.system('cls')
    typingPrint("=========== This Option For Hash Checker ===========\n")
    hash1 = input("Enter Original Hash : \n")
    hash2 = input("Enter Suspect Hash : ")
    if hash1 == hash2:
        typingPrint("\nThe Hash Is Secure")
    else:
        typingPrint("\nThe Hash Is Not Secure")
if choose == '2':
    if platform.system() == 'Linux':
        os.system('clear')
    if platform.system() == 'Windows':
        os.system('cls')
    typingPrint("=========== This Option For Hash Length Calculator ===========\n")
    length = input("Enter Your Hash : ")
    print("\nHash Length Is : ", len(length))
if choose == '3':
    if platform.system() == 'Linux':
        os.system('clear')
    if platform.system() == 'Windows':
        os.system('cls')
    typingPrint("=========== This Option For Hash Type Checker ===========\n")
    hashh = input("\nEnter The Hash : ")
    lengthh = len(hashh)
    if lengthh == 32:
        typingPrint("The Hash Is [MD5]\n")
    if lengthh == 40:
        typingPrint("The Hash Is [sha1]\n")
    if lengthh == 64:
        typingPrint("The Hash Is [sha256]")
if choose == '4':
    if platform.system() == 'Linux':
        os.system('clear')
    if platform.system() == 'Windows':
        os.system('cls')
    typingPrint("=========== This Option For MD5 Encryption ===========\n")
    word = input("\nEnter Your Text : ")
    md5 = hashlib.md5(word.encode())
    typingPrint("Your Hash : "+ md5.hexdigest())
if choose == '5':
    if platform.system() == 'Linux':
        os.system('clear')
    if platform.system() == 'Windows':
        os.system('cls')
    typingPrint("=========== This Option For MD5 Decryption ===========\n")
    hashz = input("\nEnter Your Hash : ")
    file = input("\nWrite File Name : ")
    try:
        with open(file, mode='r') as f:
            for line in f:
                line = line.strip()
                if md5(line.encode()).hexdigest() == hashz:
                    typingPrint("\n[-] Password Found :"+line)
    except:
        print("Error Occurred !\nTry Again ..")