"""
Application Configuration
"""

# Available modes:
# "system" -> Read live logs using journalctl
# "sample" -> Read logs from logs/sample_sshd.log

# comment out from system to sample for production

LOG_SOURCE = "sample"
#LOG_SOURCE = "system"

# Number of system logs to read
LOG_LIMIT = 100
