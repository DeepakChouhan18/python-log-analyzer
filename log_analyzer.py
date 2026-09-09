log_counts = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0
}

error_messages = {}

with open("sample.log", "r") as file:
    for line in file:
        if "INFO" in line:
            log_counts["INFO"] += 1

        elif "WARNING" in line:
            log_counts["WARNING"] += 1

        elif "ERROR" in line:
            log_counts["ERROR"] += 1

            error_message = line.split("ERROR", 1)[1].strip()

            if error_message in error_messages:
                error_messages[error_message] += 1
            else:
                error_messages[error_message] = 1

print("INFO:", log_counts["INFO"])
print("WARNING:", log_counts["WARNING"])
print("ERROR:", log_counts["ERROR"])

print("\nError messages:")
for error, count in error_messages.items():
    print(error, ":", count)

if error_messages:
    most_common_error = max(error_messages, key=error_messages.get)

    print("\nMost common error:")
    print(most_common_error)
    print("Occurrences:", error_messages[most_common_error])
