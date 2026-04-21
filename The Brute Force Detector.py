# The "Brute Force" Detector

class LoginAttempt:
    def __init__(self, ip_address, username, status):
        self.ip_address = ip_address
        self.username = username
        self.status = status
        
    def __repr__(self):
        return f"Attempt(IP='{self.ip_address}', Username='{self.username}', Status='{self.status}')"



class SecurityAudit:
    def __init__(self):
        self.failed_a_logs = []

    def __str__(self):
        sec_alert_rep = []
        sec_alert_rep.append(f"=== SECURITY ALERT REPORT ===")
        for alert in self.failed_a_logs:
            formated_rep = f"ALERT: {alert.status} login from {alert.ip_address} [User: {alert.username}]"
            sec_alert_rep.append(formated_rep)
        sec_alert_rep.append(f"----------------------------")
        sec_alert_rep.append(f"THREAT LEVEL: {len(self.failed_a_logs)} Failed Attempts Detected")
        
        return "\n".join(sec_alert_rep)

 # i tried to automate this function that when a object gets instantiated that it compares if the attempt is good or bad. but then it would turn into a classmethod which would be against the exercise and i was to lazy to get into it. but its possible right? to automate that
    def add_attempt(self, attempt):
        if attempt.status == "Failed":
            self.failed_a_logs.append(attempt)

    

def main():
    a1 = LoginAttempt("192.168.1.5", "admin", "Failed")
    a2 = LoginAttempt("10.0.0.1", "ayaan_m", "Success")
    a3 = LoginAttempt("10.0.0.42", "root", "Failed")

    sec_rep = SecurityAudit()

    sec_rep.add_attempt(a1)
    sec_rep.add_attempt(a2)
    sec_rep.add_attempt(a3)

    print(sec_rep)


if __name__ == "__main__":
    main()