from colorama import Fore, init
init(autoreset=True)
from socket import socket, gaierror, gethostbyname, AF_INET, SOCK_STREAM
from os import system
from path import path
from speak import speak

def scan():
	system("ipconfig > ip.txt")
	with open("ip.txt","r", encoding="utf-8") as s:
		l = s.read().strip()
	ip = ((l.split("Wi-Fi"))[-1]).split("192")
	ip = "192"+ip[1][:12]
	print(ip)
	try:
		target = gethostbyname(str(ip))
	except gaierror:
		print(f"{Fore.RED}\nName Resolution error !")

	ports = {"20":"FTP", 
				"21":"FTP", 
				"22":"SSH", 
				"23":"Telnet", 
				"25":"SMTP", 
				"53":"DNS", 
				"80":"HTTP and HTTPS", 
				"137":"NetBIOS over TCP", 
				"139":"NetBIOS over TCP", 
				"443":"HTTP and HTTPS", 
				"445":"SMB", 
				"1433":"Used by Databases", 
				"1434":"Used by Databases", 
				"3306":"Used by Databases", 
				"3389":"Remote Desktop", 
				"8080":"HTTP and HTTPS", 
				"8443":"HTTP and HTTPS"}

	print("\nScanning...",target,"on some specific ports\n")
	a =0
	for port in ports.keys():
		s = socket(AF_INET, SOCK_STREAM)
		conn = s.connect_ex((target, int(port)))
		if(not conn):
			a += 1
			print(f"{Fore.RED}Port {port} - {ports[port]} is open")
		else:
			print(f"Port {port} - {ports[port]} is closed")
		s.close()
	speak(f"Total {a} ports are opened at this IP address.")
	print(f"{Fore.YELLOW}\nTotal",a,f"{Fore.YELLOW}ports are opened at this IP address {ip}")
	print(f"{Fore.GREEN}Port scan is completed.\n")
if __name__ == "__main__":
	scan()
