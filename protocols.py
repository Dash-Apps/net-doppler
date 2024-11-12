from scapy.packet import Packet
from scapy.fields import *
#adds support for protocols not builtin to scapy

#Class for creating dummy packets with little to no information
class dummy(Packet):
    name="dummy"
    fields_desc=None
#Class for the Address Resolution protocol containing all the neccesary fields for creating packets.
class ARP(Packet):
    name="ARPpacket"
    fields_desc = [ShortField("hw_type",16),
                   ShortField("protocol_type",16),
                   ShortField("hw_len",8),
                   ShortField("protocol_len",8),
                   ShortField("operation",16),
                   ShortField("send_hw_address",6),
                   ShortField("sender_protocol_address",4),
                   ShortField("target_hw_address",6),
                   ShortField("target_protocol_address",4)]