import subprocess

def get_failed_logins():
    command = "journalctl | grep 'Failed password'"

    try:
        logs = subprocess.check_output(command, shell=True)
        return logs.decode()
    except subprocess.CalledProcessError:
        return "No failed login attempts found."

if __name__ == "__main__":
    logs = get_failed_logins()
    print("Failed Login Attempts:\n")
    print(logs)
