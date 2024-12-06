import scapy.all as scapy
import re
#checks availability of all protocols and returns all results
def check_protocols(ip,timeout,verbose=False):
    packet = scapy.IP(dst=ip,proto=(0,255))
    ans,unans = scapy.sr(packet,timeout=timeout,verbose=verbose)
    return ans,unans

#performs an xmas scan and returns a list of open and closed ports
def xmas(ip,timeout,verbose=False):
    open_ports=[]
    closed_ports = []
    packet= scapy.IP(dst=ip)/scapy.TCP(flags="FPU")
    ans, unans = scapy.sr(packet,timeout=timeout,verbose=verbose )
    for answer in ans:
        if re.search("RA$",str(answer.answer),):
           closed_ports.append(str(answer.answer))
    for unanswer in unans:
        open_ports.append(unanswer)
    return open_ports,closed_ports

