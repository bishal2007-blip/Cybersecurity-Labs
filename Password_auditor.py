import sys

print("--- IDENTITY ASSURANCE: PASSWORD POLICY AUDITOR ---")
# Prompt the user to type a password securely
user_password = input("Enter a password to audit for vulnerabilities: ")

# Metric 1: Track character variety (Entropy)
has_upper = any(c.isupper() for c in user_password)
has_lower = any(c.islower() for c in user_password)
has_digit = any(c.isdigit() for c in user_password)
has_special = any(not c.isalnum() for c in user_password)

# Score calculation out of 5
security_score = 0
vulnerabilities = []

# Audit Rule 1: Length
if len(user_password) >= 8:
        security_score += 2
elif len(user_password) >= 6:
        security_score += 1
        vulnerabilities.append("Password length is under the recommended 8-character threshold.")
else:
        vulnerabilities.append("CRITICAL: Password is dangerously short (under 6 characters).")

# Audit Rule 2: Complexity Mix
if has_upper and has_lower and has_digit and has_special:
        security_score += 2
elif (has_upper or has_lower) and has_digit:
        security_score += 1
        vulnerabilities.append("Missing special characters or case variations.")
else:
        vulnerabilities.append("Weak complexity profile: Lacks baseline character variation.")

# Audit Rule 3: Historical Leak Check
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
        security_score = 0 # Fail entirely if it is actively leaked
        vulnerabilities.append("CRITICAL FAILURE: Password found in historical breach dictionary!")

# Display Report
print("\n---------------- AUDIT REPORT ----------------")
print(f"Overall Risk Assessment Score: {security_score} / 5")

if security_score >= 4:
        print("🔒 STATUS: STRONG. Passwords meets defensive policy criteria.")
elif security_score >= 2:
        print("⚠️ STATUS: MEDIUM RISK. Fix recommendations below.")
else:
        print("❌ STATUS: HIGH RISK / VULNERABLE. Do not deploy.")

if vulnerabilities:
        print("\nIdentified Exposures & Recommendations:")
        for threat in vulnerabilities:
                print(f" - {threat}")
