import sys
import os

from cx_Freeze import setup, Executable

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
        version = "0.7",
        author = "Team 9",
        description = "Porter Simulation for Hamilton Health Sciences",
        options = {"build_exe": {"includes": includes,
                                 "excludes": excludes,
                                 "packages": packages,
                                 "path": path
                                }
        },
        executables = [
            Executable(
                "GUI.py",
                #shortcutName="Porter Simulation",
                #shortcutDir=desktop,
                #targetName = "PorterSimulation.exe",
                #icon="icon.ico"
            )
            ]
        )