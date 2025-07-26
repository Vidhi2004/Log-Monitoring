import os
from datetime import datetime

log_folder = "./logs"
alert_keywords = ["ERROR", "CRITICAL", "WARNING"]

def parse_logs():
    files = sorted(os.listdir(log_folder))
    if not files:
        print("No logs found.")
        return

    latest_file = os.path.join(log_folder, files[-1])
    print(f"🔍 Scanning {latest_file}")

    with open(latest_file, "r") as f:
        for line in f:
            if any(word in line for word in alert_keywords):
                print(f"[{datetime.now()}] ⚠️ ALERT: {line.strip()}")

if __name__ == "__main__":
    parse_logs()
