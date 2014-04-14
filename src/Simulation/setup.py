import sys
import os
import winshell

from cx_Freeze import setup, Executable

includefiles = ['hhs.png','dashboard.xlsm']
includes = []
excludes = []
packages = []
path = []

userhome = os.path.expanduser('~')
desktop = userhome + '\Desktop'

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"


setup(  name = "Porter Simulation",
        version = "1.0",
        author = "Team 9",
        description = "Porter Simulation for Hamilton Health Sciences",
        options = {"build_exe": {"includes": includes,
                                 "excludes": excludes,
                                 "packages": packages,
                                 'include_files': includefiles,
                                 "path": path
                                }
        },
        executables = [
            Executable(
                "GUI.py",
                shortcutName="Porter Simulation",
                shortcutDir="DesktopFolder",
                icon="icon.ico",
                targetName="PorterSimulation2014.exe",
                base = base
            )
            ]
        )
