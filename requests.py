import scapy.all as scapy
import protocols
import itertools

def arp_request(ip):
    ans, unans = scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst=ip), timeout=2)
    print(ans,unans)
#makes a tcp request for the given dport(s) and sends it to the specified host
def tcp_request(ip,dports,timeout=30,flags="",verbose=False):
    packet = scapy.IP(dst=ip)/scapy.TCP(dport=dports,flags=flags)
    ans,unans = scapy.srp(packet,timeout=timeout)
    if verbose == True:
        return ans.summary(),unans.summary()
    return ans,unans
#makes a udp request for the given 
def udp_request(ip,dports,timeout=30,flags="",verbose=False):
    packet = scapy.IP(dst=ip)/scapy.UDP(dport=dports)
    ans,unans=scapy.sr(packet,timeout=timeout)
    if verbose == True:
        return ans.summary(),unans.summary()
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
