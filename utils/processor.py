from utils.scorer import calculate_score
from utils.lead_priority import lead_priority



def process_lead(lead):


    lead.score = calculate_score(lead)
    priority = lead_priority(lead)

    return lead, priority