# WAC software

# Library

import tkinter as tk
from winreg import *
import os
from tkinter import *
from PIL import ImageTk
import sys
import win32com.shell.shell as shell
import webbrowser


# Admin access

ASADMIN = 'asadmin'

if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    sys.exit(0)
with open("somefilename.txt", "w") as out:
    print(out, "i am root")


# Texts

text_updated = 'Your system windows update is disable, Please reboot your system.'
text_updatee = 'Your system windows update is enable, Please reboot your system.'
text_defenderd = 'Your system windows defender is disable, Please reboot your system.'
text_defendere = 'Your system windows defender is enable, Please reboot your system.'
text_help = "This is a software for help you.\n" \
            "\n"\
            "Disable Update: for disable windows 10 automatic update.\n"\
            "Enable Update: for enable windows 10 automatic update.\n"\
            "Disable Defender: for disable windows defender.\n"\
            "Enable Defender: for disable windows enable.\n"\
            "Reboot: After each of the above operations,\n you need to reboot your system.\n" \
            "This is a shortcut button for this task."
text_contactus = "Contact information MIMTech\n"\
            "\n"\
            "Email: Support@mimtech.ir\n" \
            "Phone: +98011-42260276"

# GUI

root = tk.Tk()
root.title("WAC")

canvas1 = tk.Canvas(root, width=680, height=500)
canvas1.pack(expand=YES, fill=BOTH)

image = ImageTk.PhotoImage(file="WACBack.png")
canvas1.create_image(1, 1, image=image, anchor=NW)

photo = PhotoImage(file=r"wac.png")
root.iconphoto(False, photo)


# Add image for help and contact us

helpimage = PhotoImage(file=r"help image.png")
contactusimage = PhotoImage(file=r"contact us.png")


# Disable maximize button

root.resizable(0, 0)


# Function/Operation

def text(x):
    label1 = tk.Label(root, text=x, fg='#FAFF75', bg='#001322', bd=2, relief=FLAT, width=58,  font=('SegoeUI', 8))
    canvas1.create_window(409, 432, window=label1)


def help_text():
    label1 = tk.Label(root, text=text_help, image=helpimage, anchor=CENTER, bd=2, relief=FLAT, fg='white',
                      bg="#046272", width=320,
                      height=213,
                      font=('SegoeUI', 8))
    canvas1.create_window(409, 199, window=label1)


def contact_us():
    label1 = tk.Label(root, text=text_contactus, image=contactusimage, anchor=CENTER, bd=2, relief=FLAT, fg='white',
                      bg="#046272", width=320,
                      height=65,
                      font=('SegoeUI', 8))
    canvas1.create_window(408, 366, window=label1)


def update_disable():
    # Step1
    key = OpenKey(HKEY_LOCAL_MACHINE, r'SOFTWARE\Policies\Microsoft\Windows', 0, KEY_ALL_ACCESS)
    CreateKey(key, "WindowsUpdate")

    # Step2
    key = OpenKey(HKEY_LOCAL_MACHINE, r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate', 0, KEY_ALL_ACCESS)
    CreateKey(key, "AU")

    # Step3
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE, r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU', 0, KEY_ALL_ACCESS)
        SetValueEx(key, "AUOptions", 0, REG_DWORD, 0x00000002)
        CloseKey(key)
        text(text_updated)
    except:
        print("Disabling the update did not work.")


def update_enable():
    # Step1
    key = OpenKey(HKEY_LOCAL_MACHINE, r'SOFTWARE\Policies\Microsoft\Windows', 0, KEY_ALL_ACCESS)
    CreateKey(key, "WindowsUpdate")

    # Step2
    key = OpenKey(HKEY_LOCAL_MACHINE, r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate', 0, KEY_ALL_ACCESS)
    CreateKey(key, "AU")

    # Step3
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE, r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU', 0, KEY_ALL_ACCESS)
        SetValueEx(key, "AUOptions", 0, REG_DWORD, 0x00000000)
        CloseKey(key)
        text(text_updatee)
    except:
        print("Activating the update did not work.")


def defender_disable():
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE, r'SOFTWARE\Policies\Microsoft\Windows Defender', 0, KEY_ALL_ACCESS)
        SetValueEx(key, "DisableAntiSpyware", 0, REG_DWORD, 0x00000001)
        text(text_defenderd)
    except:
        print("Disabling the defender did not work.")


def defender_enable():
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE, r'SOFTWARE\Policies\Microsoft\Windows Defender', 0, KEY_ALL_ACCESS)
        SetValueEx(key, "DisableAntiSpyware", 0, REG_DWORD, 0x00000000)
        text(text_defendere)
    except:
        print("Activating the defender did not work.")


def reboot():
    os.system("shutdown /r /t 1")


def web():
    webbrowser.open('http://mimtech.ir/mag/disable-win10-update/')


# Click

Help = tk.Button(text='Help', width=14, command=help_text, bg='white', fg='#001322', bd=2, relief=FLAT,
                 font=('SegoeUI', 9))
canvas1.create_window(131, 99, window=Help)

updated = tk.Button(text='Disable Update', width=14, command=update_disable, bg='white', bd=2, fg='#001322',
                    relief=FLAT, font=('SegoeUI', 9))
canvas1.create_window(131, 140, window=updated)

updatee = tk.Button(text='Enable Disable', width=14, command=update_enable, bg='white', bd=2, fg='#001322', relief=FLAT,
                    font=('SegoeUI', 9))
canvas1.create_window(131, 181, window=updatee)

defenderd = tk.Button(text='Disable Defender', width=14, command=defender_disable, bg='white', bd=2, fg='#001322',
                      relief=FLAT, font=('SegoeUI', 9))
canvas1.create_window(131, 223, window=defenderd)

defendere = tk.Button(text='Enable Defender', width=14, command=defender_enable, bg='white', bd=2, fg='#001322',
                      relief=FLAT, font=('SegoeUI', 9))
canvas1.create_window(131, 265, window=defendere)

reboot = tk.Button(text='Reboot', width=14, command=reboot, bg='white', bd=2, fg='#001322', relief=FLAT,
                   font=('SegoeUI', 9))
canvas1.create_window(131, 308, window=reboot)

Contactus = tk.Button(text='Contact US', width=14, command=contact_us, bg='white', bd=2, fg='#001322', relief=FLAT,
                      font=('SegoeUI', 9))
canvas1.create_window(131, 350, window=Contactus)

web_page = tk.Button(text='Web page', width=14, command=web, bg='white', bd=2, fg='#001322', relief=FLAT,
                     font=('SegoeUI', 9))
canvas1.create_window(131, 391, window=web_page)

root.mainloop()
