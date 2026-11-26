# Mission 03 — System Inspection Evidence

Sanitized observation log recorded on macOS during system inspection exercises.

## 1. Operating System Details
```text
$ sw_vers
ProductName:        macOS
ProductVersion:     27.2
BuildVersion:       26B123
```

## 2. Root Volume Storage Snapshot
```text
$ df -h /
Filesystem       Size   Used  Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1  460Gi   13Gi  327Gi     4%    487k  3.4G    0%   /
```

## 3. System Load & Activity Snapshot
```text
$ uptime
23:38  up 9:05, 1 user, load averages: 2.45 2.10 1.95
```
System is operating under low resource pressure with abundant disk space available.
