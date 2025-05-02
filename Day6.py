import socket
from datetime import datetime
#comment
# Step 1: Port Scanning Function
def scan_port(host, port):
    try:
        # Create a socket (IPv4, TCP)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Wait max 1 second for response
        result = sock.connect_ex((host, port))  # Returns 0 if port is open
        sock.close()
        return result == 0  # True if open, False if closed/filtered
    except:
        return False  # Error occurred (port likely filtered)

# Step 2: Logging Function
def log_scan(port, status, service):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M]")
    log_entry = f"{timestamp} Port {port} {status} ({service})\n"
    
    # Append results to log file
    with open("scan_log.txt", "a") as f:
        f.write(log_entry)
        # Special warning for open SSH (security risk)
        if port == 22 and status == "open":
            f.write(f"{timestamp} WARNING: SSH port open - Brute-force attack risk!\n")

# Step 3: Main Scanner
def main():
    host = "127.0.0.1"  # Scan your own machine (localhost)
    ports = {
        21: "FTP",
        22: "SSH",
        25: "SMTP",
        80: "HTTP",
        443: "HTTPS",
        3306: "MySQL",
        3389: "RDP",
        8080: "HTTP-Alt",
        8888: "Jupyter",
        27017: "MongoDB"
    }
    
    print(f"Scanning {host}...")
    for port, service in ports.items():
        if scan_port(host, port):
            status = "open"
            print(f"Port {port} ({service}): \033[92mOPEN\033[0m")  # Green color
        else:
            status = "closed"
            print(f"Port {port} ({service}): \033[91mCLOSED\033[0m")  # Red color
        log_scan(port, status, service)
    
    print("Results saved to scan_log.txt")

if __name__ == "__main__":
    main()
