# python-tools
Security scripts and tools written in Python to learn how they work

####Python Port Scanner

## Description
This project is a TCP port scanner written in Python using the `socket` module. It allows users to scan a set of common ports or test a specific port on a given target IP or hostname. The goal of this project was to learn how basic port scanning works at the socket level and to reflect on how tools like Nmap behave differently than hand-built scanners.

## Features
- Scan common TCP ports (80, 443, 21, 22, 23, 25, 53, 8080, 445, 88)
- Option to scan a **single specific port**
- Uses `socket.connect()` for TCP connection testing
- Displays open or closed status for each scanned port
- Includes safety features (timeout, clean output)

## How to Run

In terminal use command: python port_scanner.py

You'll be prompted to:
- Enter the target IP or hostname
- Choose between scanning common ports or one specific port (Options 1 or 2)

## Results Of My Test Environments

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

## 🙌 Author
Faith Aikhionbare
Cybersecurity student + builder  
Project: Phase 1 of custom 3-week cybersecurity roadmap