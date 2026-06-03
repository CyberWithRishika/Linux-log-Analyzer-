# Linux Log Analyzer

filename = input("Enter log file path: ")

try:
    with open(filename, "r") as file:
        lines = file.readlines()

    failed_logins = 0

    for line in lines:
        if "Failed password" in line:
            failed_logins += 1

    print("\nSecurity Report")
    print("----------------")
    print("Failed login attempts:", failed_logins)

except FileNotFoundError:
    print("Log file not found!")
