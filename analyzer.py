import re
import json
from datetime import datetime

LOG_FILE = "sample_logs/auth.log"
THRESHOLD = 5  # número de tentativas para gerar alerta

failed_pattern = re.compile(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)")

ip_attempts = {}

def severity_level(attempts):
    if attempts >= 10:
        return "High"
    elif attempts >= 6:
        return "Medium"
    else:
        return "Low"

def generate_alert(ip, attempts):
    alert = {
        "alert_type": "SSH Brute Force",
        "source_ip": ip,
        "attempts": attempts,
        "severity": severity_level(attempts),
        "mitre": {
            "technique_id": "T1110",
            "technique_name": "Brute Force",
            "tactic": "Credential Access"
        },
        "recommended_action": [
            "Bloquear IP no firewall",
            "Verificar tentativas em outros serviços",
            "Reforçar política de senha"
        ],
        "timestamp": datetime.now().isoformat()
    }

    filename = f"alert_{ip.replace('.', '_')}.json"
    with open(filename, "w") as f:
        json.dump(alert, f, indent=4)

    print(f"[ALERTA GERADO] {filename}")

def analyze():
    with open(LOG_FILE, "r") as file:
        for line in file:
            match = failed_pattern.search(line)
            if match:
                ip = match.group(1)
                ip_attempts[ip] = ip_attempts.get(ip, 0) + 1

    for ip, attempts in ip_attempts.items():
        if attempts >= THRESHOLD:
            generate_alert(ip, attempts)

if __name__ == "__main__":
    analyze()
