count = 0

# Open the log file (read-only)
with open("server_logs.txt", "r") as file:
    print("========== CYBERSECURITY SECURITY ALERTS ==========\n")

    # Open the report file (write mode)
    with open("security_report.txt", "w") as report:

        report.write("========== SECURITY REPORT ==========\n\n")
        report.write("Suspicious Activities Detected:\n\n")

        # Check every line in the log file
        for line in file:

            # Detect failed login attempts
            if "Failed login attempt" in line:
                count += 1

                alert = "SUSPICIOUS ACTIVITY DETECTED: " + line.strip()

                # Print to terminal
                print(alert)

                # Save to report
                report.write(alert + "\n")

        # Add summary to the report
        report.write("\n=====================================\n")
        report.write(f"Total Failed Login Attempts: {count}\n")
        report.write("Report generated successfully.\n")

# Print summary to terminal
print("\n=====================================")
print(f"Total Failed Login Attempts: {count}")
print("Security report saved as 'security_report.txt'")
