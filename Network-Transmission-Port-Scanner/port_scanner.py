import socket

# Legal testing target provided by Nmap
target_host = "scanme.nmap.org"

# List of common ports to scan
ports_to_scan = [22, 80, 443, 8080]

# Counter for open ports
open_ports = []

print(f"========== STARTING NETWORK PORT AUDIT ON: {target_host} ==========\n")
print("Scanning channels for active exposures...\n")

# Create the report file
with open("port_scan_report.txt", "w") as report:

    report.write("========== PORT SCAN REPORT ==========\n\n")
    report.write(f"Target Host: {target_host}\n\n")
    report.write("Scan Results:\n\n")

    for port in ports_to_scan:

        # Create TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2.0)

        # Attempt connection
        result = s.connect_ex((target_host, port))

        if result == 0:
            message = f"OPEN: Port {port} is accessible."
            print(f"🔓 {message}")
            report.write(message + "\n")
            open_ports.append(port)

        else:
            message = f"CLOSED: Port {port} is closed or filtered."
            print(f"🔒 {message}")
            report.write(message + "\n")

        s.close()

    # Summary
    report.write("\n=====================================\n")
    report.write(f"Total Ports Scanned: {len(ports_to_scan)}\n")
    report.write(f"Open Ports Found: {len(open_ports)}\n")

    if open_ports:
        report.write("Open Ports: " + ", ".join(map(str, open_ports)) + "\n")
    else:
        report.write("No open ports detected.\n")

    report.write("Report generated successfully.\n")

print("\n=====================================")
print(f"Total Ports Scanned: {len(ports_to_scan)}")
print(f"Open Ports Found: {len(open_ports)}")
print("Report saved as 'port_scan_report.txt'")
print("PORT SCAN COMPLETE.")
