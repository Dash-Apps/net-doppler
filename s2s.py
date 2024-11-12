import netmiko
from scapy.all import *
import protocols

#functions to allow for, and gather data important to, server to server communication
supported_protocols = ["CAN,UDP,TCP"]
#ping a single host and wait for response
def ping(protocol,host):
    pass
#discover and ping all hosts running on a server
def ping_all():
    pass

#check what protocols are allowed for the target server
def check_protocols():
    pass