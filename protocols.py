from scapy.packet import Packet
from scapy.fields import *
#adds support for protocols not builtin to scapy

#Class for creating dummy packets with little to no information
class dummy(Packet):
    name="dummy"
    fields_desc=[]
