import socket
import struct
import sys

class DnsClient:
    def __init__(self, domainName): #  domainName = hostname
        self.domainName = domainName

        # DNS Query Header
        self.TransactionId = 1
        self.Flag = 0x0100
        self.Questions = 1
        self.AnswerRRs = 0
        self.AuthorityRRs = 0
        self.AdditionalRRs = 0
    
    # processing dns response
    def response(self, packet):  # packet : 받는 패킷 (똑같이 생성)
        dnsHeader = packet[:12]  # 앞 12bytes 버림 (필요 없음)
        dnsData = packet[12:].split(b'\x00', 1)  # \x00(널문자)을 기준으로 1번 분할 함

        ansRR = packet[12+len(dnsData[0])+5:12+len(dnsData[0])+21]
        rr_unpack = struct.unpack('!2sHHIH4s', ansRR)
        ip_addr = socket.inet_ntoa(rr_unpack[5])
        print(self.domainName, ip_addr)

    # creat dns query
    def query(self):
        # DNS header packing
        # 총 12bytes
        query = struct.pack('!HH', self.TransactionId, self.Flag)
        query += struct.pack('!HH', self.Questions, self.AnswerRRs)
        query += struct.pack('!HH', self.AuthorityRRs, self.AdditionalRRs)

        part = self.domainName.split('.')
        # ex) www.google.co.kr >> part = [www, google, co, kr]

        for i in range(len(part)):
            query = query + struct.pack('!B', len(part[i]))  # i = 0, wwww -> len = 3 
            query = query + part[i].encode()  # part[i].encode() = www에 해당되는 ASCII값

        query = query + b'\x00'  # 끝났다는 의미

        query_type = 1 # Type: A
        query_class = 1 # Class: IN
        query = query + struct.pack('!HH', query_type, query_class)

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        addr = ('220.69.193.130', 53)   # 순천향대학교 DNS 서버 주소
        sock.sendto(query, addr)  # 서버로 전송
        packet, address = sock.recvfrom(65535)  # 서버에서 수신
        self.response(packet)

if __name__ == '__main__':
    if len(sys.argv) > 1 :  # hostname이 있으면
        client = DnsClient(sys.argv[1])  # Client 객체 만듦
        client.query()

