# python-tools
Security scripts and tools written in Python to learn how they work

## Tools in this Repo
- [Port Scanner](#-python-port-scanner-Tool)
- [Log Parser](#-log-parser-tool)
- [Recon-Report] (#-Reconnaissance-Practice-Report-(Learning-Folder))
- [Upcoming: Brute Forcer...]

# 🔍 Python Port Scanner Tool

## 📄 Description
This project is a TCP port scanner written in Python using the `socket` module. It allows users to scan a set of common ports or test a specific port on a given target IP or hostname. The goal of this project was to learn how basic port scanning works at the socket level and to reflect on how tools like Nmap behave differently than hand-built scanners.

## 🛠 Features
- Scan common TCP ports (80, 443, 21, 22, 23, 25, 53, 8080, 445, 88)
- Option to scan a **single specific port**
- Uses `socket.connect()` for TCP connection testing
- Displays open or closed status for each scanned port
- Includes safety features (timeout, clean output)

## 🧪 How to Run

```bash
python port_scanner.py
```

You'll be prompted to:
- Enter the target IP or hostname
- Choose between scanning common ports or one specific port (Options 1 or 2)

## 🖥️ Results Of My Test Environments

### 1. **Localhost (127.0.0.1)**
- Most ports returned as **Closed** (expected)
- After running a Python HTTP server on port 8080, scanner still showed port 8080 as **Closed**
- **Root cause:** Python's `http.server` defaulted to IPv6 (`[::]`) while the scanner used IPv4 sockets → mismatched address families

### 2. **Public Target (`scanme.nmap.org`)**
- Some ports like 22 and 80 were correctly detected as **Open**
- Others like 23, 443 returned **Closed** (normal behavior for that host)
- Showed that scanner can connect over internet and resolve DNS hostnames properly

### 3. **Windows Server 2022 VM**
- Nmap showed many ports as **Open**: 53, 88, 135, 139, 445, 5357, 5985
- Scanner initially reported **88 and 445 as Closed**, then later reported them as **Open**
- Scanner correctly detected port 53 as Open

## Debugging Discoveries

### Challenge: Port 88 and Port 445
- Scanning these individually sometimes returned **Closed**, even though Nmap showed **Open**
- Scanning them in a **batch of common ports** returned them as **Open**
- This inconsistency helped me understand:
  - Protocols like **Kerberos (88)** or **SMB (445)** may not accept generic TCP connects
  - `socket.connect()` behaves differently than Nmap’s `-sS` SYN scans
  - Some ports are sensitive to timing or how the TCP handshake is initiated

### Challenge: HTTP server on localhost not detected
- Python HTTP server (`python -m http.server 8080`) was running and accessible by browser
- Scanner still said port 8080 was **Closed**
- Root cause: server was binding to IPv6 (`[::]`) and scanner was using IPv4 (`127.0.0.1`)
- Resolution: learned to check how services bind (IPv4 vs IPv6 mismatch)

## 🧠 What I Learned
- How to use Python's `socket` module for basic TCP connections
- What “open” vs “closed” ports really mean in practice
- How real-world systems (like Windows VMs) can behave differently than expected
- That Nmap uses lower-level probing which is more protocol-aware and flexible than a basic socket scan
- How DNS resolution works in Python when scanning hostnames
- How to document and reflect on challenges during a security project

## 📌 Future Ideas
- Add multithreading for faster scans
- Handle IPv6 scanning
- Export results to a `.txt` or `.json` file
- Handle connection timeouts with retry logic 


# 🔍 Log Parser Tool

A simple Python script that scans and analyzes Apache-style log files to identify failed login attempts, suspicious activity, and frequently active IP addresses.

## 📄 What It Does
This tool reads through a web server log file line by line and extracts:
- Total number of log entries scanned  
- Number of **failed login attempts** (status codes `401`, `403`, or `404`)  
- The **top 5 IP addresses** by total requests  
- Suspicious activity is written to `suspicious_logs.log`

## 🧠 What I Learned
- How Apache-style log files are structured  
- How to use `regex` to extract key log fields (IP, timestamp, request, status code)  
- How to identify failed login attempts or suspicious paths  
- How attackers might hide in "noisy" logs  
- How to build simple alert logic using Python and `Counter`

## 🧪 Example Log Line Parsed
192.168.1.5 - - [15/Dec/2025:14:52:10] "GET /admin HTTP/1.1" 403 498

From this, the parser extracts:
- IP: `192.168.1.5`  
- Timestamp: `15/Dec/2025:14:52:10`  
- Request: `GET /admin HTTP/1.1`  
- Status Code: `403`

## ⚙️ How to Use

#### ✅ Run the script:

```bash
python log_parser.py access.log
```
Replace access.log with path to your log file. Use access.log to test using my test log file. 

# Reconnaissance Practice Report (Learning Folder)

As part of my Phase 1 roadmap, I created a `learning-recon/` folder where I ran common reconnaissance tools and documented the process with **screenshots** and a professional-style **Recon Report**.

## 💻 Tools Used
All commands were run in **WSL (Windows Subsystem for Linux)** inside Ubuntu. This helped me practice in a Linux-based terminal environment while working on a Windows host system.

## 🔍 Recon Report Summary
The report focused on the public host `scanme.nmap.org`, which is provided by Nmap for educational purposes.

## ✅ Passive Recon
Tools used:
- `whois`
- `nslookup`
- `dig`

Findings:
- `whois` returned info about IP ownership, including phone numbers, links, and domain dates, but scanme.nmap.org did not show all the info because it is a test machine for port scanning. 
- `nslookup` returned hostnames and resolved IPs.
- `dig` showed more technical DNS info and flags, although I found the output harder to read at first.

## ✅ Active Recon
Tools used:
- `traceroute`
- `ping`
- Custom `port_scanner.py`

Findings:
- `traceroute` showed **20 hops** from my computer to scanme.nmap.org (latency: ~85.7ms)
- `ping` confirmed that the target was reachable
- My port scanner confirmed open ports (80, 22) and reinforced what I had learned about socket behavior

## 🧠 What I Learned
- **Reconnaissance** is the *initial phase* of cybersecurity investigations. A way to gather information to understanda system before deeper analysis or exploitation.
- **Passive Recon** means gathering public info from the system (e.g., DNS lookups).
- **Active Recon** means gathering data by sending packets or creating traffic (e.g., port scanning).
- I learned about **IP addresses**, **DNS servers**, and **how attackers or analysts gather this data** to understand a system.
- I also realized that **recon reports** are used like *periodic health checks* before/after incidents and are not really done daily, but they are done often.

## 💥 Challenges Faced
- My **Windows Server 2022 VM** gave errors when trying to install WSL. So I used my host machine’s Ubuntu WSL to run tools instead.
- Some tools like `dig` had unfamiliar output (UDP flags, TTL, etc.), but I still learned to recognize server IPs and DNS data.
- I had never created a professional-style recon report before, but I learned how to structure and document it effectively.

## 🖼️ Screenshot Evidence
All screenshots of commands and outputs are stored in the `learning-recon/screenshots/` folder for reference.

## 📄 Report File
A Markdown version of the full **Reconnaissance Report** is included in `learning-recon/recon_report.md`.

🧠 **Reflection Summary:**
This hands-on recon activity helped me move beyond theory and understand how professional cybersecurity workflows begin. It connected to:
- **Digital forensics**
- **System health checks**
- **Pre-exploitation intelligence**
- And how to analyze output from common Linux tools.


## 🙌 Author
Faith Aikhionbare
Cybersecurity student + builder  
Project: Phase 1 of custom 3-week cybersecurity roadmap