import argparse
import socket
from typing import List


def scan_ports(host: str, start_port: int, end_port: int) -> List[int]:
    """Scan a range of ports on the given host and return a list of open ports."""
    open_ports = []
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
    return open_ports


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple port scanner")
    parser.add_argument("host", help="Host to scan, e.g., 127.0.0.1")
    parser.add_argument("--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("--end", type=int, default=1024, help="End port (default: 1024)")
    parser.add_argument("--connect", type=int, help="Port to connect to after scanning")
    args = parser.parse_args()

    print(f"Scanning ports {args.start}-{args.end} on {args.host}...")
    open_ports = scan_ports(args.host, args.start, args.end)
    if open_ports:
        print("Open ports found:", ", ".join(map(str, open_ports)))
    else:
        print("No open ports found in the specified range.")

    if args.connect:
        if args.connect in open_ports:
            print(f"Attempting to connect to {args.host}:{args.connect}...")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                try:
                    sock.settimeout(2)
                    sock.connect((args.host, args.connect))
                    print(f"Successfully connected to {args.host}:{args.connect}")
                except OSError as exc:
                    print(f"Connection failed: {exc}")
        else:
            print(f"Port {args.connect} is not open or not in the scanned range.")


if __name__ == "__main__":
    main()
