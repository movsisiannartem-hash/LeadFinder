def lead_priority(lead):
    if lead.score >= 5:
        return "HOT"
    elif 3 <= lead.score <= 4:
        return "WARM"
    elif lead.score == 2:
        return "COLD"
    elif lead.score < 2:
        return "LOW"
