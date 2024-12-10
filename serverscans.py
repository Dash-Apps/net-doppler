import scapy.all as scapy
import re
#checks availability of all protocols and returns all results
def check_protocols(ip,timeout,verbose=False):
    #makes ip header packets for every single protocol and sends them
    packet = scapy.IP(dst=ip,proto=(0,255))
    ans,unans = scapy.sr(packet,timeout=timeout,verbose=verbose)
    return ans,unans

#performs an xmas scan and returns a list of open and closed ports
def xmas(ip,dports,timeout,verbose=False):
    open_ports=[]
    closed_ports = []
    #creates tcp packet with the Fin Push and Urgent flags set aimed at the specified dport
    packet= scapy.IP(dst=ip)/scapy.TCP(flags="FPU",dport=dports)
    #sends the packet with timeout and verbose arguments
    ans, unans = scapy.sr(packet,timeout=timeout,verbose=verbose )
    #for each answer received check if it returned with the reset and ack flags
    # if it did add it to the closed ports list
    for response in ans:
        if response.answer[scapy.TCP].flags =="RA":
           closed_ports.append(str(response.answer))
    #add any unanswered packets to the open ports list
    for unanswer in unans:
        open_ports.append(unanswer)
    #return both the open and closed ports list
    return open_ports,closed_ports
#someone who reads this remind me to change it to use sr so it can accept host ranges otherwise it works fine when using the echo port and localhost address
def sa_scan(target_ip, dport,timeout):
    pkt = scapy.IP(dst=target_ip) / scapy.TCP(dport=dport, flags='S')  # SYN packet
    response = scapy.sr1(pkt, timeout=timeout, verbose=0)
    if response and response.haslayer(scapy.TCP) and response[scapy.TCP].flags == "RA" or "SA":  # SYN-ACK response or RST-ACK response
        print(f"[+] Closed Port: {dport} : {response}")
    else:
        print(f"[+] Open Port: {dport} : {response}")
