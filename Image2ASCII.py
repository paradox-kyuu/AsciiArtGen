from PIL import Image
import pywhatkit
import os
import random
from colorama import Fore,Style
import pyfiglet
import time

all_col= [Style.BRIGHT+Fore.RED,Style.BRIGHT+Fore.CYAN,Style.BRIGHT+Fore.LIGHTCYAN_EX, Style.BRIGHT+Fore.LIGHTBLUE_EX, Style.BRIGHT+Fore.LIGHTCYAN_EX,Style.BRIGHT+Fore.LIGHTMAGENTA_EX,Style.BRIGHT+Fore.LIGHTYELLOW_EX, Style.BRIGHT+Fore.WHITE]

ran = random.choice(all_col)


def banner():
    print(ran, pyfiglet.figlet_format("\t\t\t  AsciiArtGen V1.0"))
    print(ran + "\t\t        V_1.0\t\n\n")
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX, "\n\t    ", "- " * 3, "BY PARADOX-KYUU ", "- " * 3)
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX, "\n", "- " * 3, " Github: https://github.com/paradox-kyuu ", "- " * 3)
    print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX, "\n [!] AsciiArtGenV1.0 is an Image to Ascii Art Generator. [!]")
	

banner()

image_file = input("\n\nEnter path to Image: ")
image_name= input("\n\nSave as (Name only): ")

print(Style.BRIGHT + Fore.LIGHTBLUE_EX, "\n", "- " * 3, " Converting Image to Ascii Art ", "- " * 3)
time.sleep(1)
print(Style.BRIGHT + Fore.LIGHTBLUE_EX, "\n", "- " * 3, " Ascii Art saved as: \"" + image_name + ".txt\"", "- " * 3)

time.sleep(2)
print("\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=\n")
print(Style.BRIGHT + Fore.LIGHTBLUE_EX, "\t" + image_name + ".txt")
print("\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=\n")
time.sleep(1)
Image.open(image_file)
pywhatkit.image_to_ascii_art(image_file, image_name)
read_file = open(image_name + ".txt", 'r')
print(Style.BRIGHT + Fore.WHITE, read_file.read())

