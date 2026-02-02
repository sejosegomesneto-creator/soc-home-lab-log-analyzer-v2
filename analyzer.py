import re
from collections import Counter

LOG_FILE = "sample_logs/auth.log"

def analyze_log(file_path):
    with open(file_path, "r") as file:
        logs = file.readlines()

    failed_logins = []
    success_logins = []

    for line in logs:
        if "Failed password" in line:
            failed_logins.append(line)
        elif "Accepted password" in line:
            success_logins.append(line)

    return failed_logins, success_logins

def extract_ips_from_failed(failed_logins):
    ips = []
    for line in failed_logins:
        match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
        if match:
            ips.append(match.group(1))
    return ips

def generate_report(failed, success):
    print("=== SOC HOME LAB REPORT (v2) ===\n")
    print(f"Falhas de login: {len(failed)}")
    print(f"Acessos bem-sucedidos: {len(success)}\n")

    ips = extract_ips_from_failed(failed)
    if ips:
        counter = Counter(ips)
        print("IPs com mais tentativas de falha:")
        for ip, count in counter.most_common(5):
            print(f"- {ip}: {count} tentativas")
    else:
        print("Nenhum IP encontrado nas falhas.")

if __name__ == "__main__":
    failed, success = analyze_log(LOG_FILE)
    generate_report(failed, success)

