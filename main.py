from collector.log_reader import get_logs
from collector.log_filter import filter_logs, print_summary


def main():

    logs = get_logs()

    suspicious_logs = filter_logs(logs)

    print_summary(suspicious_logs)


if __name__ == "__main__":
    main()
