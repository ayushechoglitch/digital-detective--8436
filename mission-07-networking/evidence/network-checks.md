# Mission 07 — Network Checks Evidence

Sanitized observation logs from live network tests conducted on macOS.

## 1. DNS Resolution Log
```text
$ nslookup example.com
Server:        [redacted-local-resolver]
Address:       [redacted]#53

Non-authoritative answer:
Name:   example.com
Address: 104.20.23.154
Name:   example.com
Address: 172.66.147.243
```

## 2. Ping Connectivity & Latency Log
```text
$ ping -c 4 example.com
PING example.com (104.20.23.154): 56 data bytes
64 bytes from 104.20.23.154: icmp_seq=0 ttl=56 time=23.546 ms
64 bytes from 104.20.23.154: icmp_seq=1 ttl=56 time=24.567 ms
64 bytes from 104.20.23.154: icmp_seq=2 ttl=56 time=37.521 ms
64 bytes from 104.20.23.154: icmp_seq=3 ttl=56 time=23.745 ms

--- example.com ping statistics ---
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 23.546/27.345/37.521/5.888 ms
```
