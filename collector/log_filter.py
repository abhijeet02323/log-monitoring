"""
------------------------------------------------------------
Cloud Log Monitoring System
Module: Log Filter
Version: 1.1

Description:
Filters suspicious SSH authentication events from raw logs.
------------------------------------------------------------
"""

from typing import List


# Keywords considered suspicious
SUSPICIOUS_KEYWORDS = [
    "Failed password",
    "Failed publickey",
    "Invalid user",
    "authentication failure",
    "error: maximum authentication attempts exceeded",
    "Connection closed by authenticating user",
]


def is_suspicious(log_line: str) -> bool:
    """
    Check whether a log entry contains suspicious activity.

    Args:
        log_line (str): Single log line.

    Returns:
        bool: True if suspicious, False otherwise.
    """

    log_line = log_line.lower()

    return any(keyword.lower() in log_line for keyword in SUSPICIOUS_KEYWORDS)


def filter_logs(logs: List[str]) -> List[str]:
    """
    Filter all suspicious logs.

    Args:
        logs (List[str]): List of raw log entries.

    Returns:
        List[str]: Only suspicious log entries.
    """

    filtered = []

    for log in logs:
        if is_suspicious(log):
            filtered.append(log)

    return filtered


def print_summary(filtered_logs: List[str]) -> None:
    """
    Print summary of filtered logs.
    """

    print("\n========== Security Log Summary ==========")
    print(f"Suspicious Events Found : {len(filtered_logs)}")

    if not filtered_logs:
        print("Status : No suspicious activity detected.")
        return

    print("\nDetected Events:\n")

    for index, log in enumerate(filtered_logs, start=1):
        print(f"{index}. {log.strip()}")


if __name__ == "__main__":

    sample_logs = [
        "Accepted publickey for ec2-user from 10.0.0.15",
        "Failed publickey for invalid user admin from 192.168.1.20",
        "Connection closed by authenticating user root",
        "Starting OpenSSH server",
        "Failed password for root from 172.16.10.50",
    ]

    suspicious_logs = filter_logs(sample_logs)

    print_summary(suspicious_logs)
