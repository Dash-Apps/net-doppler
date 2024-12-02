import scapy.all as scapy
import protocols
import itertools
#functions to allow for, and gather data important to, server to server communication
supported_protocols = ["CAN,UDP,TCP"]
#ping a single host and wait for response
def ping(host):
    request = scapy.IP(dst=host)/scapy.TCP(dport=[21,22,23])
    res,unans = scapy.sr(request) 
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
def packet_sniff(amount=0):
    #if no amount of packets is entered, sniff forever until the loop is broken.
    if amount == 0:
        while True:
            scapy.sniff(count=1).summary()
    #otherwise sniff for the amount specified
    else:
        scapy.sniff(count=amount).summary()
    #sniffs one packet at a time for display purposes when running infinitely

packet_sniff(amount=10)