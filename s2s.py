import scapy.all as scapy
import protocols
import itertools

#makes a tcp request for the given dport(s) and sends it to the specified host
def tcp_request(ip,dports,flags=""):
    packet = scapy.IP(dst=ip)/scapy.TCP(dport=dports)
    ans,unans = scapy.sr(packet)
    return ans,unans

#gains the ip of your device
def self_ip():
    packet = scapy.IP()
    return packet.show()
#attempts to fetch the ip of a given website url   
def get_website_ip(domain):
    dns_req = scapy.IP(dst="8.8.8.8")/scapy.UDP(dport=53)/scapy.DNS(rd=1, qd=scapy.DNSQR(qname=domain))
    dns_resp = scapy.sr1(dns_req, timeout=2, verbose=0)

    if dns_resp and dns_resp.haslayer(scapy.DNS):
        return dns_resp[scapy.DNS].an.rdata
    else:
        return None
#check what protocols are allowed for the target server
def check_protocols():
    pass
#utilizes scapys packet sniffing function for monitoring network traffic
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
tcp_request("127.0.0.1",[7])