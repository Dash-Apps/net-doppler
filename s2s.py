import scapy.all as scapy
import protocols
import itertools
#functions to allow for, and gather data important to, server to server communication
supported_protocols = ["CAN,UDP,TCP"]
#gains the ip of your device
def self_ip():
    packet = scapy.IP()
    print(packet)
#attempts to fetch the ip of a given website url   
def get_website_ip(domain):
    dns_req = scapy.IP(dst="8.8.8.8")/scapy.UDP(dport=53)/scapy.DNS(rd=1, qd=scapy.DNSQR(qname=domain))
    dns_resp = scapy.sr1(dns_req, timeout=2, verbose=0)

    if dns_resp and dns_resp.haslayer(scapy.DNS):
        return dns_resp[scapy.DNS].an.rdata
    else:
        return None

#pings a single host by performing a tcp handshake
def ping(host):
    request = scapy.IP(dst=host)/scapy.TCP(dport=[21,22,23])
    res = scapy.send(request) 
    return res

def ping_multiple(target_list):
    pass
#discover and ping all hosts running on a server by performing a an tcp handshake request broadcast
def ping_all(ip,range):
    request = scapy.IP(dst=ip)/scapy.TCP(dport=[21,22,23])
  
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
            scapy.sniff(prn=packet_callback)
    #otherwise sniff for the amount specified
    else:
        scapy.sniff(prn=packet_callback,count=amount)
def packet_callback(packet):
    print(packet.show())
