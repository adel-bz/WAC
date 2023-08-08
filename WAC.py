# WAC Software

# Librarys
from winreg import *
import os
from tkinter import *
from PIL import ImageTk
import customtkinter
import webbrowser

# Constants for image paths
WINUPDATE_DIS_IMAGE_PATH = "assets/winupdate_dis_image.png"
WINUPDATE_ENA_IMAGE_PATH = "assets/winupdate_ena_image.png"
DEFENDER_DIS_IMAGE_PATH = "assets/defender_dis_image.png"
DEFENDER_ENA_IMAGE_PATH = "assets/defender_ena_image.png"
RESTART_IMAGE_PATH = "assets/restart.png"
WEBSITE_IMAGE_PATH = "assets/website.png"
GITHUB_IMAGE_PATH = "assets/github.png"
HELP_IMAGE_PATH = "assets/help.png"

# Buttons oprations result texts
### Successful ###
successful_texts = {
    "winupdate_dis_operation": "Windows Update service was disabled.\nPlease reboot your system.",
    "winupdate_ena_operation": "Windows Update service was enabled.\nPlease reboot your system.",
    "defender_dis_operation": "Windows Defender was disabled.\nPlease reboot your system.",
    "defender_ena_operation": "Windows Defender was enabled.\nPlease reboot your system."
}

### Unsuccessful ###
unsuccessful_texts = {
    "winupdate_dis_operation": "Disabling Windows Update was unsuccessful.",
    "winupdate_ena_operation": "Enabling Windows Update was unsuccessful.",
    "defender_dis_operation": "Disabling Windows Defender was unsuccessful",
    "defender_ena_operation": "Enabling Windows Defender was unsuccessful"
}

# GUI
### Creating a window ###
root= customtkinter.CTk(fg_color="#1C3754") 
 
### Title ###
title_text = "WAC"
root.title('{: >91}'.format(title_text)) 

### Set icon & Disabling resizable ###
root.resizable(0, 0)
root.iconbitmap("assets/WAC-icon.ico")

### The window configs & Background ###
bg = ImageTk.PhotoImage(file="assets/WACBack.png")
my_Canvas = Canvas(root, width=645, height=500)
my_Canvas.pack(expand=True, fill=BOTH)
my_Canvas.create_image(0, 0, image=bg ,anchor=NW)

### The Lable configs for showing results text ###
label = customtkinter.CTkLabel(root, text="")
my_Canvas.create_window(420, 225, window=label)

def display_result(result_text):
    global label
    label.destroy()
    label = customtkinter.CTkLabel(root, text=result_text, fg_color="transparent", bg_color='transparent',
                                  anchor=NW, font=('Poppins', 11, "normal"))
    my_Canvas.create_window(420, 225, window=label)
    
# Buttons Operation
### Windows 'update disabling' button operation: 
## Disables Windows Update with appropriate registry key settings and shows the result. ###
def winupdate_dis_operation():
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
        display_result(successful_texts["winupdate_dis_operation"])
    except Exception:
        CloseKey(key)
        display_result(unsuccessful_texts["winupdate_dis_operation"])

### Windows 'update enabling' button operation:
## Enables Windows Update with the relevant registry key values and displays the result. ###
def winupdate_ena_operation():
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
        display_result(successful_texts["winupdate_ena_operation"])
    except Exception:
        CloseKey(key)
        display_result(unsuccessful_texts["winupdate_ena_operation"])

### Windows 'defender disabling' button operation:
## Disables Windows Defender by modifying the registry, and the result is shown. ###
def defender_dis_operation():
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE, r'SOFTWARE\Policies\Microsoft\Windows Defender', 0, KEY_ALL_ACCESS)
        SetValueEx(key, "DisableAntiSpyware", 0, REG_DWORD, 0x00000001)
        CloseKey(key)
        display_result(successful_texts["defender_dis_operation"])
    except Exception:
        CloseKey(key)
        display_result(unsuccessful_texts["defender_dis_operation"])

### Windows 'defender enabling' button operation: 
## Enables Windows Defender through registry changes, and the outcome is displayed. ###
def defender_ena_operation():
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE, r'SOFTWARE\Policies\Microsoft\Windows Defender', 0, KEY_ALL_ACCESS)
        SetValueEx(key, "DisableAntiSpyware", 0, REG_DWORD, 0x00000000)
        CloseKey(key)
        display_result(successful_texts["defender_ena_operation"])
    except Exception:
        CloseKey(key)
        display_result(unsuccessful_texts["defender_ena_operation"])

### Restart button operation: Initiates a system restart with a delay of 2 second. ###
def restart_operation():
    os.system("shutdown /r /t 2")

### Website button operation: Opens a web link to an external resource about disabling Windows 10 update. ###
def website_operation():
    webbrowser.open('https://mimtech.ir/mag/disable-win10-update/')

### Github button operation: Opens a web link to the GitHub repository for WAC. ###
def github_operation():
    webbrowser.open('https://github.com/adel-bz/WAC')

### Help button operation: Opens a web link for GitHub support. ###
def help_operation():
    webbrowser.open('https://github.com/adel-bz/WAC#buttons-and-operations')

# Buttons: 
## In this section, buttons are created for various operations in the Graphical User Interface (GUI) of the WAC Software. 
## Each button is associated with an image and a specific operation, 
## and clicking the button triggers the corresponding action. 
## The buttons are positioned on the canvas, and their positions are determined using coordinates. ##

# Buttons creation
def create_button(image_path, command):
    image = ImageTk.PhotoImage(file=image_path)
    button = customtkinter.CTkButton(master=root, image=image, text="",
                                     fg_color="transparent", bg_color="transparent",
                                     hover_color="#4E749F", corner_radius=0, border_width=1,
                                     border_color="#1C3754", command=command)
    return button

### Disabling update button ###
winupdate_dis_button = create_button(WINUPDATE_DIS_IMAGE_PATH, winupdate_dis_operation)
my_Canvas.create_window(50, 58, window=winupdate_dis_button ,anchor=NW)

### Enabling update button ###
winupdate_ena_button = create_button(WINUPDATE_ENA_IMAGE_PATH, winupdate_ena_operation)
my_Canvas.create_window(50, 107, window=winupdate_ena_button ,anchor=NW)

### Disabling defender button ###
defender_dis_button = create_button(DEFENDER_DIS_IMAGE_PATH, defender_dis_operation)
my_Canvas.create_window(50, 156, window=defender_dis_button ,anchor=NW)

### Enabling defender button ###
defender_ena_button = create_button(DEFENDER_ENA_IMAGE_PATH, defender_ena_operation)
my_Canvas.create_window(50, 205, window=defender_ena_button ,anchor=NW)

### Restart button ###
restart_button = create_button(RESTART_IMAGE_PATH, restart_operation)
my_Canvas.create_window(50, 254, window=restart_button ,anchor=NW)

### Website button ###
website_button = create_button(WEBSITE_IMAGE_PATH, website_operation)
my_Canvas.create_window(50, 303, window=website_button ,anchor=NW)

### Github button ###
github_button = create_button(GITHUB_IMAGE_PATH, github_operation)
my_Canvas.create_window(50, 352, window=github_button ,anchor=NW)

### Help button ###
help_button = create_button(HELP_IMAGE_PATH, help_operation)
my_Canvas.create_window(50, 401, window=help_button ,anchor=NW)

# Loop Window
root.mainloop()