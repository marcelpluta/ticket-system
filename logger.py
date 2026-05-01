from datetime import datetime

def log_ticket(ticket, priority):
    with open("tickets_log.txt", "a") as f:
        f.write(f"{datetime.now()} | ID:{ticket['id']} | {ticket['issue']} | Severity:{ticket['severity']} | {priority}\n")
