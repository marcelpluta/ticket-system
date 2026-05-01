def get_priority(ticket):
    if ticket["severity"] >= 8:
        return "CRITICAL"
    elif ticket["severity"] >= 5:
        return "HIGH"
    elif ticket["severity"] >= 3:
        return "MEDIUM"
    else:
        return "LOW"
