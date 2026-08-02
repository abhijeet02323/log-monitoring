"""
------------------------------------------------------------
Cloud Log Monitoring System

Module:
    Sample SSH Log Generator

Description:
    Generates realistic SSH authentication logs for
    development and testing purposes.

Author:
    Abhijeet Dwivedi

Version:
    1.0
------------------------------------------------------------
"""

import random
from datetime import datetime, timedelta
from pathlib import Path


OUTPUT_FILE = Path("logs/sample_sshd.log")

NUMBER_OF_LOGS = 100


HOSTNAME = "ip-172-31-43-12"

SERVICE = "sshd"


VALID_USERS = [
    "ec2-user",
    "ubuntu",
    "admin",
    "developer",
    "john",
    "alice"
]


INVALID_USERS = [
    "root",
    "guest",
    "oracle",
    "test",
    "mysql",
    "backup",
    "anonymous"
]


SUCCESS_EVENTS = [
    "Accepted publickey for {user} from {ip} port {port} ssh2",
    "Accepted password for {user} from {ip} port {port} ssh2"
]


FAILED_EVENTS = [
    "Failed password for {user} from {ip} port {port} ssh2",
    "Failed publickey for invalid user {user} from {ip} port {port} ssh2",
    "Invalid user {user} from {ip} port {port}",
    "authentication failure; rhost={ip}",
    "Connection closed by authenticating user {user} {ip} port {port} [preauth]"
]


MONTHS = [
    "Jan", "Feb", "Mar", "Apr",
    "May", "Jun", "Jul", "Aug",
    "Sep", "Oct", "Nov", "Dec"
]


def random_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))


def random_port():
    return random.randint(1024, 65535)


def random_time():

    start = datetime.now() - timedelta(days=7)

    end = datetime.now()

    delta = end - start

    random_seconds = random.randint(
        0,
        int(delta.total_seconds())
    )

    timestamp = start + timedelta(seconds=random_seconds)

    return timestamp


def build_timestamp(timestamp):

    month = MONTHS[timestamp.month - 1]

    return (
        f"{month} "
        f"{timestamp.day:02d} "
        f"{timestamp.strftime('%H:%M:%S')}"
    )


def generate_log():

    timestamp = random_time()

    log_time = build_timestamp(timestamp)

    pid = random.randint(1000, 9000)

    is_success = random.random() < 0.4

    if is_success:

        template = random.choice(SUCCESS_EVENTS)

        user = random.choice(VALID_USERS)

    else:

        template = random.choice(FAILED_EVENTS)

        if "invalid user" in template.lower() or "Invalid user" in template:
            user = random.choice(INVALID_USERS)
        else:
            user = random.choice(VALID_USERS)

    message = template.format(
        user=user,
        ip=random_ip(),
        port=random_port()
    )

    return (
        f"{log_time} "
        f"{HOSTNAME} "
        f"{SERVICE}[{pid}]: "
        f"{message}"
    )


def generate_logs():

    OUTPUT_FILE.parent.mkdir(exist_ok=True)

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        logs = [
            generate_log()
            for _ in range(NUMBER_OF_LOGS)
        ]

        logs.sort()

        for log in logs:
            file.write(log + "\n")

    print("=" * 55)
    print("Cloud Log Monitoring System")
    print("=" * 55)
    print(f"Generated Logs : {NUMBER_OF_LOGS}")
    print(f"Output File    : {OUTPUT_FILE}")
    print("Status         : SUCCESS")
    print("=" * 55)


if __name__ == "__main__":
    generate_logs()
