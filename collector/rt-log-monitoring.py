import subprocess

def get_failed_logs():
    print(" Fetching system logs...\n")

    command = "journalctl -u sshd -n 100"

    try:
        logs = subprocess.check_output(command, shell=True).decode()
        filtered_logs = []

        for line in logs.split("\n"):
            if "Failed" in line or "Invalid user" in line:
                filtered_logs.append(line)

        if filtered_logs:
            print(" Detected Suspicious Activities:\n")
            for log in filtered_logs:
                print(log)
        else:
            print("No suspicious activity found.")

        return filtered_logs

    except subprocess.CalledProcessError:
        print(" Error fetching logs.")
        return []


if __name__ == "__main__":
    get_failed_logs()

def format_log(log):
    parts = log.split()
    ip = parts[-4] if len(parts) > 5 else "Unknown"
    return f"IP: {ip} | Event: {log}"
for log in filtered_logs:
    print(format_log(log))
