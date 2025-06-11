from collections import Counter

def detect_breach(log_file):
    with open(log_file, 'r') as file:
        lines = file.readlines()

    failed_ips = []
    for line in lines:
        if "FAILED LOGIN" in line:
            ip = line.strip().split()[-1]
            failed_ips.append(ip)

    if failed_ips:
        failed_counter = Counter(failed_ips)
        print("🚨 Potential security breaches detected:\n")
        print(f"{'IP Address':<20}Failed Attempts")
        print("-" * 35)
        for ip, count in failed_counter.items():
            print(f"{ip:<20}{count}")
    else:
        print("✅ No breaches detected.")

if __name__ == "__main__":
    detect_breach('web_activity_log.txt')
