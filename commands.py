import os
import platform
import subprocess
#functions for parsing data from CLI commands 

#get os type using the platform library
def get_os():
    return platform.uname().system
#finds your ip using CLI commands
def get_ip():
    if get_os() == "Linux":
        output = subprocess.Popen([], stdout=subprocess.PIPE).communicate()[0]
