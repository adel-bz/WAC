# Introduction
The WAC (Windows Assistant Controller) software is a utility designed for controlling various settings of the Windows operating system. This document provides an overview and explanation of the code structure and functionality of the WAC software. 
The software is built using Python and leverages several libraries and modules to interact with the Windows Registry, create a graphical user interface (GUI), and perform various system operations.

![Screenshot from 2023-08-16 10-30-25](https://github.com/adel-bz/WAC/assets/45201934/7d724078-74f5-4139-8cbc-24571075ce8b)



# Code Structure
## Libraries and Modules Used
The WAC software relies on the following libraries and modules:

`winreg:` This module is used to work with the Windows Registry, allowing the software to modify registry keys.

`os:` This module is used for performing system-level operations, such as initiating a system restart.

`tkinter:` This module is used to create the graphical user interface (GUI) for the application.
PIL (Python Imaging Library): This library is used for image handling and manipulation.

`customtkinter:` This is a custom library that enhances the capabilities of the default tkinter library.

`webbrowser:` This module is used to open URLs in the default web browser.

## Image Paths
The code uses constants to define the paths of various image assets. These images are used for buttons and other graphical elements in the GUI.

## Result Texts
The software provides descriptive texts to display the results of different operations. There are texts defined for both successful and unsuccessful outcomes of various operations, such as enabling or disabling Windows Update or Windows Defender.

## Graphical User Interface (GUI)
The GUI of the WAC software is created using the tkinter library. The main window is customized with specific properties, including an icon and a background image. The results of operations are displayed using customtkinter labels. 

Buttons are used to trigger different operations, and each button is associated with a specific function. The GUI is designed to be user-friendly and intuitive

# Buttons and Operations
The software offers several buttons, each associated with a specific operation. Here are the available operations:

`Disabling Windows Update:` This operation disables the Windows Update service by modifying registry keys.

`Enabling Windows Update:` This operation enables the Windows Update service by modifying registry keys.

`Disabling Windows Defender:` This operation disables Windows Defender by modifying registry keys.

`Enabling Windows Defender:` This operation enables Windows Defender by modifying registry keys.

`Restarting System:` This operation initiates a system restart with a delay of 2 seconds.

`Website:` This button opens a web link to an external resource about disabling Windows 10 updates.

`GitHub:` This button opens a web link to the GitHub repository for the WAC software.

`Help:` This button opens a web link for GitHub support related to the software.

# Usage
The user interface is designed to provide an intuitive experience for users. When a button is clicked, the corresponding operation is performed, and the result of the operation is displayed in a label on the GUI. Successful operations show success messages, while unsuccessful operations display corresponding error messages.

You can download WAC from releases.

# Libraries Documentations

https://docs.python.org/3/library/winreg.html

https://docs.python.org/3/library/os.html

https://docs.python.org/3/library/tk.html

https://customtkinter.tomschimansky.com/documentation/

https://docs.python.org/3/library/webbrowser.html

# Conclusion
The WAC software offers a user-friendly way to control various settings of the Windows operating system. It provides operations to disable or enable Windows Update and Windows Defender, along with other functionalities. The graphical user interface makes it easy for users to interact with the software and receive feedback on their actions. This document provides an overview of the code structure and functionality of the WAC software.
