import socket
import struct
import binascii

class Udphdr:
    def __init__(self, sport, dport, length, checksum):
        self.sport = sport
        self.dport = dport
        self.length = length
        self.checksum = checksum


    def pack_Udphdr(self):
        packed = b''
        packed += struct.pack('!HH', self.sport, self.dport) 
        packed += struct.pack('!HH', self.length, self.checksum) 
        # packed += struct.pack('!4H', self.sport, self.dport, self.length, self.checksum)  
        return packed
    
def unpack_Udphdr(buffer):
    unpacked = struct.unpack('!4H', buffer[:20])
    return unpacked

def getSrcPort(unpacked_udpheader):
    return unpacked_udpheader[0]

def getDstPort(unpacked_udpheader):
    return unpacked_udpheader[1]

def getLength(unpacked_udpheader):
    return unpacked_udpheader[2]

def getChecksum(unpacked_udpheader):
    return unpacked_udpheader[3]

udp = Udphdr(5555, 80, 1000, 0xFFFF)
# 2bytes로 pack된 bytes 객체
packed_udphdr = udp.pack_Udphdr()
print(binascii.b2a_hex(packed_udphdr))

unpacked_udphdr = unpack_Udphdr(packed_udphdr)
print(unpacked_udphdr)
print('Source Port:{} Destination Port:{} Length:{} Checksum:{}'\
    .format(getSrcPort(unpacked_udphdr), getDstPort(unpacked_udphdr), 
            getLength(unpacked_udphdr), getChecksum(unpacked_udphdr)))