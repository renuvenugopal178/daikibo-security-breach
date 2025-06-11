def detect_breach(log_file):
    with open(log_file, 'r') as file:
        lines = file.readlines()

    suspicious_ips = []
    for line in lines:
        if "FAILED LOGIN" in line:
            ip = line.split()[-1]  # assumes IP is last word in line
            suspicious_ips.append(ip)

    if suspicious_ips:
        print("Potential security breach detected from IPs:")
        for ip in set(suspicious_ips):
            print(ip)
    else:
        print("No breaches detected.")

if __name__ == "__main__":
    detect_breach('web_activity_log.txt')
