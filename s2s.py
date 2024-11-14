import netmiko
from scapy.all import *
import protocols

#functions to allow for, and gather data important to, server to server communication
supported_protocols = ["CAN,UDP,TCP"]
#ping a single host and wait for response
def ping(protocol,host):
    icmp_packet = IP(dst=host) / ICMP()
    sr1(icmp_packet)
    response = sr1(icmp_packet, timeout=1)
#discover and ping all hosts running on a server
def ping_all():
    request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)

    ans, unans = srp(request, timeout=2, retry=1)
    result = []

    for sent, received in ans:
        result.append({'IP': received.psrc, 'MAC': received.hwsrc})

    return result

#check what protocols are allowed for the target server
def check_protocols():
    pass
