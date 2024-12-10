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
    for answer in ans:
        if re.search("RA$",str(answer.answer),):
           closed_ports.append(str(answer.answer))
    #add any unanswered packets to the open ports list
    for unanswer in unans:
        open_ports.append(unanswer)
    #return both the open and closed ports list
    return open_ports,closed_ports
    
def scan_port(target_ip, port):
    pkt = IP(dst=target_ip) / TCP(dport=port, flags='S')  # SYN packet
    response = sr1(pkt, timeout=1, verbose=0)
    if response and response.haslayer(TCP) and response[TCP].flags == 0x12:  # SYN-ACK response
        print(f"[+] Open Port: {port}")

