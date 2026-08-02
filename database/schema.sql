-- =====================================================
-- Cloud Log Monitoring System
-- Database Schema v1.1
-- PostgreSQL
-- =====================================================

-- Drop existing table (for development only)
DROP TABLE IF EXISTS ssh_logs;

-- =====================================================
-- SSH Logs Table
-- =====================================================

CREATE TABLE ssh_logs (

    id SERIAL PRIMARY KEY,

    -- Date and time of the log event
    event_time TIMESTAMP NOT NULL,

    -- Username involved in the event
    username VARCHAR(100),

    -- IP Address of the client
    ip_address INET,

    -- SSH Port
    port INTEGER,

    -- Authentication method
    authentication_method VARCHAR(50),

    -- Event Type
    -- Examples:
    -- Failed Password
    -- Failed PublicKey
    -- Invalid User
    -- Accepted Password
    event_type VARCHAR(100) NOT NULL,

    -- Log severity
    severity VARCHAR(20) DEFAULT 'INFO',

    -- SSH service name
    service VARCHAR(50) DEFAULT 'sshd',

    -- Complete original log
    raw_log TEXT NOT NULL,

    -- Timestamp when inserted into database
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================================
-- Indexes
-- =====================================================

CREATE INDEX idx_event_time
ON ssh_logs(event_time);

CREATE INDEX idx_ip_address
ON ssh_logs(ip_address);

CREATE INDEX idx_username
ON ssh_logs(username);

CREATE INDEX idx_event_type
ON ssh_logs(event_type);

-- =====================================================
-- Comments
-- =====================================================

COMMENT ON TABLE ssh_logs IS
'Stores parsed SSH authentication logs collected from Linux journalctl';

COMMENT ON COLUMN ssh_logs.event_time IS
'Timestamp when the SSH event occurred';

COMMENT ON COLUMN ssh_logs.ip_address IS
'Source IP address';

COMMENT ON COLUMN ssh_logs.raw_log IS
'Original journalctl log entry';
