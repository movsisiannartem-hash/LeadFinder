import json
from dataclasses import asdict
from models import Lead

def save_leads_to_json(leads, filename):
    with open(filename, 'w', encoding="utf-8") as file:
        data = [asdict(lead) for lead in leads]
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_leads_from_json(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        data = json.load(file)
        leads = []
        for item in data:
            lead = Lead(**item)
            leads.append(lead)
    return leads