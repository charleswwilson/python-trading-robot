import socket
from IPy import IP  


def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def scan_port(ipaddress, port):

    try:
        sock = socket.socket()
        sock.settimeout(.5)
        sock.connect((ipaddress, port))
        print(f'[+] Port {port} is Open')

    except:
        print(f'[-] Port {port} Is Closed')


ipaddress = input('[+] Enter Target To Scan: ')

converted_ip = check_ip(ipaddress)

for port in range(1,200):

    scan_port(converted_ip,port)