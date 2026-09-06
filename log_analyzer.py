log_counts = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0
}

with open("sample.log", "r") as file:
    for line in file:
        if "INFO" in line:
            log_counts["INFO"] += 1
        elif "WARNING" in line:
            log_counts["WARNING"] += 1
        elif "ERROR" in line:
            log_counts["ERROR"] += 1

print("INFO:", log_counts["INFO"])
print("WARNING:", log_counts["WARNING"])
print("ERROR:", log_counts["ERROR"])
