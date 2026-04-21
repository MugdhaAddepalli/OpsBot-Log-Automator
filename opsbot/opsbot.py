import re
import os
from datetime import datetime

# Input log file
input_file = "server.log"

# Output file with current date
date_str = datetime.now().strftime("%Y-%m-%d")
output_file = f"security_alert_{date_str}.txt"

# Keywords to search
patterns = ["CRITICAL", "ERROR", "FAILED LOGIN"]

# Dictionary to count occurrences
error_count = {
    "CRITICAL": 0,
    "ERROR": 0,
    "FAILED LOGIN": 0
}

filtered_lines = []

# Step 1: Read file
with open(input_file, "r") as file:
    for line in file:
# Step 2: Pattern matching
        for pattern in patterns:
            if re.search(pattern, line, re.IGNORECASE):
                error_count[pattern] += 1
                filtered_lines.append(line)
                break  # avoid double counting

# Step 3 & 4: Write filtered data to output file
with open(output_file, "w") as file:
    file.write("=== SECURITY ALERT REPORT ===\n\n")
    
    for line in filtered_lines:
        file.write(line)
    
    file.write("\n=== SUMMARY ===\n")
    for key, value in error_count.items():
        file.write(f"{key}: {value}\n")

# Step 5: Automation using os module
file_size = os.path.getsize(output_file)

print("Security alert file created successfully!")
print(f" File Name: {output_file}")
print(f" File Size: {file_size} bytes")

print("\nSummary:")
for key, value in error_count.items():
    print(f"{key}: {value}")