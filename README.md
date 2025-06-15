# Chapy

This repository contains a simple Python script to scan ports on a given host. It can also attempt to connect to one of the detected open ports.

## Usage

```
python3 port_scanner.py <host> [--start START_PORT] [--end END_PORT] [--connect PORT]
```

Example:

```
python3 port_scanner.py 127.0.0.1 --start 1 --end 1024 --connect 22
```

This will scan ports `1` through `1024` on `127.0.0.1` and attempt to connect to port `22` if it is open.
