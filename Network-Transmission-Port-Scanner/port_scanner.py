import socket
import sys

#legal testing target provider
target_host = "scanme.nmap.org"

# list of common standard ports we want to audit
ports_to_scan = [22, 80, 443, 8080]

print(f" STARTING NETWORK PORT AUDIT ON: {target_host} ")
print("Scanning channels for active exposures...\n")

for port in ports_to_scan:
# Set up a standard TCP network socket configuration
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2.0)

# Attempt to connect to the target host on the specific port number
        result = s.connect_ex((target_host, port))

# connect_ex returns a value of 0 if the connection handshake was successful
        if result == 0:
                print(f"🔓 ALERT: Port {port} is OPEN! Potential entry point detected.")
        else:
                print(f"🔒 Secure: Port {port} is closed or protected.")

# Close the individual socket connection to clean up network memory
        s.close()

print("PORT SCAN COMPLETE.")
