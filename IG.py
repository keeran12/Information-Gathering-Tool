import socket
from termcolor import colored
from pyfiglet import figlet_format
print((colored(figlet_format("Information Gathering Tool", font ="standard", width="15"),color="blue")))
print("-------------..version.1..--------------------by Keeran_M")
print()
print()
def gather_info(target_host):
    try:
        target_ip = socket.gethostbyname(target_host)
        print("[*] Target IP: %s" % target_ip)
       
        # get the hostname
        target_hostname = socket.gethostbyaddr(target_ip)
        print("[*] Target Hostname: %s" % target_hostname[0])
       
        # get all IP addresses for the host
        ip_list = socket.gethostbyname_ex(target_host)[2]
        for ip in ip_list:
            print("[*] IP: %s" % ip)
       
        # open a socket to the target host and port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((target_host, 80))
        print("[*] Port 80 open")
        s.close()
    except:
        print("[-] Unable to gather information")

# get target host as runtime input
target_host = input("Enter target host: ")

# gather information for the target host
gather_info(target_host)
