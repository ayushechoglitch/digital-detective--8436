# Mission 07 — Computer Networks & Internet Architecture

## 1. Mission Title & Objectives
**Title:** Networking Topologies, Protocols, and the Web Request Lifecycle  
**Objective:** Define foundational networking concepts, perform live DNS resolution and connectivity tests, analyze packet round-trip metrics, and detail the end-to-end lifecycle of a web page request.

## 2. Work Completed
### Task 7.1 — Core Networking Concepts

| Network Concept | Plain-English Definition | Real-World Concrete Example |
|---|---|---|
| **LAN (Local Area Network)** | A high-speed network connecting devices across a limited local area. | A home Wi-Fi network or university computer laboratory. |
| **MAN (Metropolitan Area Network)** | A network spanning a city or broad municipal campus area. | City-wide municipal government network or university multi-campus fiber loop. |
| **WAN (Wide Area Network)** | A large-scale network connecting disparate LANs across countries and continents. | The global public Internet. |
| **DNS (Domain Name System)** | The internet's distributed directory translating human names into numerical IP addresses. | Resolving `example.com` $ightarrow$ `104.20.23.154`. |
| **Router** | A Layer-3 network gateway that directs and forwards data packets between different subnets. | A home broadband fiber/cable router connecting home LAN to ISP WAN. |
| **Protocol** | Standardized, agreed-upon rules governing data formatting and transmission between machines. | TCP, IP, UDP, HTTP, HTTPS, TLS, SSH. |
| **Packet Switching** | Breaking data into discrete, independently addressed packets that route across shared networks. | Streaming a video or downloading a webpage over the internet. |
| **Client-Server Model** | An architectural pattern where a client requests resources and a centralized server responds. | Web browser (client) requesting an HTML document from a web server. |

---

### Task 7.2 — Live Connectivity & DNS Tests
I ran standard network inspection utilities against the public domain `example.com`:

1. **DNS Lookup (`nslookup example.com`):**
   - The query resolved to dual IPv4 A records: `104.20.23.154` and `172.66.147.243`.
   - DNS acts as the essential translation layer because human beings remember names like `example.com`, but routers and network interfaces can only route packets based on numerical binary IP addresses.

2. **Reachability Test (`ping -c 4 example.com`):**
   - Transmitted 4 ICMP Echo Request packets and received 4 ICMP Echo Replies.
   - **Packet Loss:** `0.0%` (100% transmission success).
   - **Round-Trip Latency:** Minimum: `23.5 ms`, Average: `27.3 ms`, Maximum: `37.5 ms`.

---

### Task 7.3 — What Happens When You Open a Website in a Browser?
When a user types `https://example.com` into a web browser address bar and presses Enter, a 7-step sequence unfolds:

1. **URL Parsing & Cache Check:** The browser extracts the domain name and checks local memory caches (browser DNS cache, OS resolver cache) for a recent IP entry.
2. **DNS Resolution:** If not cached, the operating system queries the local recursive DNS resolver, which traverses the DNS hierarchy (Root $ightarrow$ TLD `.com` $ightarrow$ Authoritative nameserver) to return the destination IP address (`104.20.23.154`).
3. **TCP Connection & TLS Handshake:** The browser initiates a TCP three-way handshake (`SYN`, `SYN-ACK`, `ACK`) on port 443. For secure HTTPS, a TLS cryptographic handshake negotiates ciphers, verifies the server's digital certificate, and establishes shared symmetric encryption keys.
4. **HTTP GET Request:** Over the encrypted channel, the browser transmits an HTTP request:
   ```http
   GET / HTTP/1.1
   Host: example.com
   User-Agent: Mozilla/5.0 ...
   ```
5. **Packet Routing:** The request bytes are divided into IP packets, stamped with source and destination IP addresses, and routed across multiple intermediate router hops using BGP/OSPF.
6. **Server Processing & Response:** The destination web server receives the packets, reassembles the TCP stream, processes the request, and returns an HTTP response containing headers and HTML payload:
   ```http
   HTTP/1.1 200 OK
   Content-Type: text/html; charset=UTF-8
   ```
7. **Client Rendering:** The browser layout engine parses HTML to build the DOM tree, fetches linked CSS/JavaScript assets, calculates layout geometry, and paints the final rendered webpage onto the screen.

Detailed transcripts are archived in [Network Checks Evidence](evidence/network-checks.md).

## 3. Practical Difficulties & Solutions
- **Challenge:** Understanding why ping occasionally fails on certain university/public networks even when websites load.
- **Resolution:** Learned that ping uses ICMP Echo packets, which many network firewalls block for security reasons, while standard HTTP/HTTPS traffic on ports 80/443 remains open.

## 4. Commit & Verification Status
- **Commit Message:** `Explain networking concepts and website communication`
- **Status:** Verified and pushed to `main`.
