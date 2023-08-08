# Introduction
The WAC (Windows Assistant Controller) software is a utility designed for controlling various settings of the Windows operating system. This document provides an overview and explanation of the code structure and functionality of the WAC software. The software is built using Python and leverages several libraries and modules to interact with the Windows Registry, create a graphical user interface (GUI), and perform various system operations.

# Code Structure
## Libraries and Modules Used
The WAC software relies on the following libraries and modules:

#### winreg: 
This module is used to work with the Windows Registry, allowing the software to modify registry keys.

os: This module is used for performing system-level operations, such as initiating a system restart.

tkinter: This module is used to create the graphical user interface (GUI) for the application.
PIL (Python Imaging Library): This library is used for image handling and manipulation.

customtkinter: This is a custom library that enhances the capabilities of the default tkinter library.

webbrowser: This module is used to open URLs in the default web browser.

## Image Paths
The code uses constants to define the paths of various image assets. These images are used for buttons and other graphical elements in the GUI.

## Result Texts
The software provides descriptive texts to display the results of different operations. There are texts defined for both successful and unsuccessful outcomes of various operations, such as enabling or disabling Windows Update or Windows Defender.

## Graphical User Interface (GUI)
The GUI of the WAC software is created using the tkinter library. The main window is customized with specific properties, including an icon and a background image. The results of operations are displayed using customtkinter labels. Buttons are used to trigger different operations, and each button is associated with a specific function. The GUI is designed to be user-friendly and intuitive
