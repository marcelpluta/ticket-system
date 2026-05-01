from ticket_generator import create_ticket
from priority import get_priority
from logger import log_ticket

for i in range(20):
    ticket = create_ticket()
    priority = get_priority(ticket)

    print(f"Ticket {ticket['id']} | {ticket['issue']} | Severity {ticket['severity']} → {priority}")

    log_ticket(ticket, priority)
