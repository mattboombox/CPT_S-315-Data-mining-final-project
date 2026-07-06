from scapy.all import rdpcap, TCP, Raw

packets = rdpcap('ftp_burglary.pcap')
for pkt in packets:
    # FTP-DATA usually occurs on port 20 or is identified by the Raw load
    if pkt.haslayer(Raw) and pkt.haslayer(TCP):
        payload = pkt[Raw].load.decode(errors='ignore')
        # Look for typical flag formats (e.g., flag{...} or CTF{...})
        if "flag" in payload:
            print(f"Potential Flag Found: {payload}")