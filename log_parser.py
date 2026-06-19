# Opens the log file (read-only)
with open("server_logs.txt", "r") as file:
    print(" CYBERSECURITY SECURITY ALERTS GENERATED ")

# Checks every line in the file
    for line in file:

# If the line contains a brute-force footprint, catch it
        if "Failed login attempt" in line:
# Clean up the spaces and print the suspicious activity
            print("SUSPICIOUS ACTIVITY DETECTED:", line.strip())
