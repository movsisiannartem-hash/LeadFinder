def filter_leads(leads, min_score):
    filtered_leads = []
    for lead in leads:
        if lead.score >= min_score:
            filtered_leads.append(lead)
    return filtered_leads