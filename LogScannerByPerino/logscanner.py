import datetime

# --- Configuration Settings ---
MAX_ATTEMPTS = 3
BUSINESS_HOURS_START = 9  # 09:00
BUSINESS_HOURS_END = 18   # 18:00

# Simulated log data
log_entries = [
    {"ip": "192.168.1.5", "user": "admin", "status": "failed", "time": "03:15:00"},
    {"ip": "192.168.1.5", "user": "admin", "status": "failed", "time": "03:16:00"},
    {"ip": "192.168.1.5", "user": "admin", "status": "failed", "time": "03:17:00"},
    {"ip": "10.0.0.2", "user": "staff_01", "status": "success", "time": "14:20:00"},
    {"ip": "172.16.0.45", "user": "root", "status": "success", "time": "23:45:00"},
]

def run_security_audit(logs):
    # This dictionary will store the number of failed attempts per IP
    failed_attempts_tracker = {}
    
    print(f"{'='*10} STARTING SECURITY AUDIT {'='*10}")
    print(f"Analyzing {len(logs)} log entries...\n")
    
    found_issues = False # Flag to check if we found any alerts

    for entry in logs:
        ip = entry['ip']
        status = entry['status']
        # Convert string time to a datetime object
        log_time = datetime.datetime.strptime(entry['time'], "%H:%M:%S").time()

        # 1. Detection: Brute Force / Repeated Failed IP
        if status == "failed":
            failed_attempts_tracker[ip] = failed_attempts_tracker.get(ip, 0) + 1
            
            if failed_attempts_tracker[ip] >= MAX_ATTEMPTS:
                print(f"[ALERT] Brute Force detected from IP: {ip} ({failed_attempts_tracker[ip]} attempts)")
                found_issues = True

        # 2. Detection: Out-of-Hours Activity (Success only)
        start_time = datetime.time(BUSINESS_HOURS_START, 0)
        end_time = datetime.time(BUSINESS_HOURS_END, 0)

        is_outside_hours = log_time < start_time or log_time > end_time
        
        if is_outside_hours and status == "success":
            print(f"[WARNING] Suspicious Login: User '{entry['user']}' accessed from {ip} at {entry['time']} (After Hours)")
            found_issues = True

    if not found_issues:
        print("No suspicious activity detected.")
    
    print(f"\n{'='*10} AUDIT COMPLETE {'='*10}")

if __name__ == "__main__":
    run_security_audit(log_entries)