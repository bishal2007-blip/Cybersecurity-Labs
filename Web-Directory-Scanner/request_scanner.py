import requests

# Define the target website to test.
target_url = "https://httpbin.org/status/"

print("PRINTING WEB VULNERABILITY DIRECTORY SCAN")

# Open our text file containing the hidden paths to test
with open("wordlist.txt", "r") as file:
        for line in file:
# Clean up any messy white spaces or hidden breaks from the word
                directory = line.strip()

# Build the full target link 
                full_url = target_url + directory

# Try sending an HTTP request to that web page
                try:
                        response = requests.get(full_url, timeout=5)

# If the server returns status 200, the page exists and is open!
                        if response.status_code == 200:
                                print(f"🟢 MATCH FOUND: Path /{directory} responded with status 200 (OK)")
                        else:
# Any other response code means it is closed or blocked
                                print(f"🔴 Checked: /{directory} -> Status {response.status_code}")

                except requests.exceptions.RequestException:
                        print(f"⚠️ Failed to connect to: {full_url}")
