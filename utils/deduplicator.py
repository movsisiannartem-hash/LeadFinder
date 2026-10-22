from models import Lead


def remove_duplicates(leads):
    seen = set()
    leads_unique = []

    for lead in leads:
        if lead.address:
            key = (lead.name, lead.address)
        else:
            key = (lead.name, lead.latitude, lead.longitude)

        if key not in seen:
            seen.add(key)
            leads_unique.append(lead)




    return leads_unique





