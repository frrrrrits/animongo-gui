import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico','res']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    nname = "AnimOngo",
    version = "1.0",
    description = "Animongo GUI version made with Python",
    author = "lxs7499",
    options = {'build_exe' : {
        'include_files' : files,
        'excludes': ["tkinter", "unittest", "pydoc", "PyQt6", "PySide6"],
    }},
    executables = [target]
)

# masih error, ada masalah di icon2 nya ntah
# png working fine but not with the svg