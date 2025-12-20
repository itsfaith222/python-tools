# Target Reconnaissance Report
This report summarizes the results of reconnaissance performed against scanme.nmap.org, a public sandbox target provided by the developers of Nmap. A mix of passive and active recon tools were used to gather DNS, routing, and service information.  

## 1. Target Overview
- Domain: scanme.nmap.org
- Resolved IP: 45.33.32.156
- Owner: [From Whois]

## 2. DNS Information
- Address: 45.33.32.156 
- Server: 10.255.255.254 UDP
- Owner: [From nslookup and dig] 

## 3. Traceroute Results
- Hops: 20
- Total Latency: 86.157ms
- Path:
  - Faiths_Computer.net → Home_network.home → ... → scanme.nmap.org (45.33.32.156)

## 4. Ping Test
- Packets sent: 4
- Received: 4
- Min/Avg/Max: 88.219/92.909/96.823 ms

## 5. Passive Recon Tools Used
- `whois`, `nslookup`, `dig`, 

## 6. Active Recon Tools Used
- `traceroute`, `ping`

## 7. Nmap Scan Using port_scanner.py
- Open Ports: 22 (SSH), 80 (HTTP)
- OS: Linux 3.x

## 8. Wireshark Summary
- Protocols observed: DNS, TCP, HTTP
- Target IP: 45.33.32.156
- **Traffic Observed**:
  - TCP handshake on port 80
  - HTTP GET request for `/`
- Filter used: `ip.addr == 45.33.32.156`

## 9. Key Takeaways
- Target is reachable, uses Linux OS
- Website active on port 80, no HTTPS
- Could be used for basic web exploitation lab

## 10. Personal Notes + Reflection 
- What I learned about recon: it is a way to gather information about systems/servers. It is a period health check done before diving deeper into the systems. 
- Passive Recon: is looking for information already created on the systems. 
- Active Recon: is generating data by creating packets. 

---

Analyst: Faith Aikhionbare  
Date: Dec 20, 2025
