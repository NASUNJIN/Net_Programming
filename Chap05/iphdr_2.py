import socket
import struct
import binascii

class Iphdr:
    def __init__(self, tot_len, protocol, saddr, daddr):
        self.ver_len = 0x45
        self.tos = 0
        self.tot_len = tot_len
        self.id = 0
        self.frag_off = 0
        self.ttl = 127
        self.protocol = protocol    # TCP(6)/UDP(17)
        self.check = 0
        self.saddr = socket.inet_aton(saddr)
        self.daddr = socket.inet_aton(daddr)

    def pack_Iphdr(self):
        packed = b''
        # 4바이트씩 끊어 작성 함. 총 20bytes
        packed += struct.pack('!BBH', self.ver_len, self.tos, self.tot_len)  # !BBH : 112
        packed += struct.pack('!HH', self.id, self.frag_off)                 # !HH : 22
        packed += struct.pack('!BBH', self.ttl, self.protocol, self.check)   # !BBH : 112
        packed += struct.pack('!4s', self.saddr)   # !4s = !ssss 
        packed += struct.pack('!4s', self.daddr)   # s : bytes객체를 크기 고대로 넣을 때 사용
        return packed
    
def unpack_Iphdr(buffer):
    # !BBHHHBBH4s4s: 10개 짜리 튜플 리턴
    unpacked = struct.unpack('!BBHHHBBH4s4s', buffer[:20])
    return unpacked

def getPacketSize(unpacked_ipheader):
    return unpacked_ipheader[2]

def getProtocolId(unpacked_ipheader):
    return unpacked_ipheader[6]

def getIP(unpacked_ipheader):
    src_ip = socket.inet_ntoa(unpacked_ipheader[8])
    dst_ip = socket.inet_ntoa(unpacked_ipheader[9])
    return (src_ip, dst_ip)

ip = Iphdr(1000, 6, '10.0.0.1', '11.0.0.1')
packed_iphdr = ip.pack_Iphdr()
print(binascii.b2a_hex(packed_iphdr))

unpacked_iphdr = unpack_Iphdr(packed_iphdr)
print(unpacked_iphdr)
print('Packet size:{} Protocol:{} IP:{}'\
    .format(getPacketSize(unpacked_iphdr), getProtocolId(unpacked_iphdr), getIP(unpacked_iphdr)))