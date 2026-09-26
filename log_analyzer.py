import sys


def print_report(result):
    if result is None:
        return

    print("\n========== LOG REPORT ==========")

    print("Total logs:", result["total_logs"])

    if result["total_logs"] > 0:
        print("\nLog percentages:")

        for level, count in result["log_counts"].items():
            percentage = (count / result["total_logs"]) * 100
            print(level, ":", round(percentage, 2), "%")

    print("\nLog levels:")
    for level, count in result["log_counts"].items():
        print(level, ":", count)

    print("\nError messages:")
    for error, count in result["error_messages"].items():
        print(error, ":", count)

    if result["error_messages"]:
        most_common_error = max(
            result["error_messages"],
            key=result["error_messages"].get
        )

        print("\nMost common error:")
        print(most_common_error)
        print("Occurrences:", result["error_messages"][most_common_error])

    print("\nIP addresses:")
    for ip, count in result["ip_counts"].items():
        print(ip, ":", count)

    print("\nSuspicious IPs:")
    for ip, count in result["ip_counts"].items():
        if count >= 3:
            print(ip, "->", count, "requests")

    print("================================")


def analyze_log(filename):
    log_counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    error_messages = {}
    ip_counts = {}

    try:
        with open(filename, "r") as file:
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

                if "IP:" in line:
                    ip = line.split("IP:", 1)[1].strip()

                    if ip in ip_counts:
                        ip_counts[ip] += 1
                    else:
                        ip_counts[ip] = 1

    except FileNotFoundError:
        print("Error: Log file not found.")
        return None

    total_logs = sum(log_counts.values())

    return {
        "log_counts": log_counts,
        "error_messages": error_messages,
        "ip_counts": ip_counts,
        "total_logs": total_logs
    }


if len(sys.argv) < 2:
    print("Please provide a log file.")
else:
    result = analyze_log(sys.argv[1])
    print_report(result)
