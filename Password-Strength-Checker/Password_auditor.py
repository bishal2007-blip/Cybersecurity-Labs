print("--- IDENTITY ASSURANCE: PASSWORD POLICY AUDITOR ---")

# Prompt the user to type a password
user_password = input("Enter a password to audit for vulnerabilities: ")

# Character diversity checks
has_upper = any(c.isupper() for c in user_password)
has_lower = any(c.islower() for c in user_password)
has_digit = any(c.isdigit() for c in user_password)
has_special = any(not c.isalnum() for c in user_password)

# Score and findings
security_score = 0
vulnerabilities = []

# Rule 1: Password Length
if len(user_password) >= 8:
    security_score += 2
elif len(user_password) >= 6:
    security_score += 1
    vulnerabilities.append("Password length is under the recommended 8-character threshold.")
else:
    vulnerabilities.append("CRITICAL: Password is dangerously short (under 6 characters).")

# Rule 2: Password Complexity
if has_upper and has_lower and has_digit and has_special:
    security_score += 2
elif (has_upper or has_lower) and has_digit:
    security_score += 1
    vulnerabilities.append("Missing special characters or case variations.")
else:
    vulnerabilities.append("Weak complexity profile: Lacks baseline character variation.")

# Rule 3: Breach Dictionary Check
breach_found = False

try:
    with open("common_breaches.txt", "r") as database:
        for line in database:
            if user_password.strip() == line.strip():
                breach_found = True
                break
except FileNotFoundError:
    print("⚠️ Warning: Breach database dictionary missing.")

if not breach_found:
    security_score += 1
else:
    security_score = 0
    vulnerabilities.append("CRITICAL FAILURE: Password found in historical breach dictionary!")

# Display Results
print("\n---------------- AUDIT REPORT ----------------")
print(f"Overall Risk Assessment Score: {security_score} / 5")

if security_score >= 4:
    status = "STRONG"
    print("🔒 STATUS: STRONG. Password meets defensive policy criteria.")
elif security_score >= 2:
    status = "MEDIUM RISK"
    print("⚠️ STATUS: MEDIUM RISK. Fix recommendations below.")
else:
    status = "HIGH RISK"
    print("❌ STATUS: HIGH RISK / VULNERABLE. Do not deploy.")

if vulnerabilities:
    print("\nIdentified Exposures & Recommendations:")
    for threat in vulnerabilities:
        print(f"- {threat}")

# Generate Security Report
with open("password_audit_report.txt", "w") as report:

    report.write("========== PASSWORD SECURITY AUDIT REPORT ==========\n\n")
    report.write(f"Password Length: {len(user_password)} characters\n")
    report.write(f"Security Score: {security_score} / 5\n")
    report.write(f"Overall Status: {status}\n\n")

    report.write("Character Analysis:\n")
    report.write(f"- Uppercase Present : {has_upper}\n")
    report.write(f"- Lowercase Present : {has_lower}\n")
    report.write(f"- Numbers Present   : {has_digit}\n")
    report.write(f"- Special Characters: {has_special}\n")
    report.write(f"- Found in Breach Database: {breach_found}\n\n")

    if vulnerabilities:
        report.write("Recommendations:\n")
        for threat in vulnerabilities:
            report.write(f"- {threat}\n")
    else:
        report.write("No vulnerabilities detected.\n")

    report.write("\n==============================================\n")
    report.write("Password audit completed successfully.\n")

print("\n==============================================")
print("Security report saved as 'password_audit_report.txt'")
