from scapy.all import *
import protocols
import itertools
#functions to allow for, and gather data important to, server to server communication
supported_protocols = ["CAN,UDP,TCP"]
#ping a single host and wait for response
def ping(host):
    request = IP(dst=host)/TCP(dport=[21,22,23])
    res,unans = sr(request) 
    return res,unans

def ping_multiple(target_list):
    pass
#discover and ping all hosts running on a server
def ping_all(target,range):
    request = scapy.ARP(target) 
  
    request.pdst = range #network range
    broadcast = scapy.Ether() 

    broadcast.dst = 'ff:ff:ff:ff:ff:ff'
  
    request_broadcast = broadcast / request 
    clients = scapy.srp(request_broadcast, timeout = 1)[0] 
    return clients
#check what protocols are allowed for the target server
def check_protocols():
    pass

