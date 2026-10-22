import csv
from models import Lead

def save_leads_to_csv(leads, filename):
    with open(filename, 'w', newline='', encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "name",
                "description",
                "phone",
                "website",
                "address",
                "website_working",
                "social_links",
                "score",
                "latitude",
                "longitude"

            ]
        )

        writer.writeheader()
        for lead in leads:
            writer.writerow({
                "name": lead.name,
                "description": lead.description,
                "phone": lead.phone,
                "website": lead.website,
                "address": lead.address,
                "website_working": lead.website_working,
                "social_links": ", ".join(lead.social_links),
                "score": lead.score,
                "latitude": lead.latitude,
                "longitude": lead.longitude,

            })

def load_leads_from_csv(filename):
    with open(filename, 'r', newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        leads = []
        for row in reader:
            lead = Lead(
                name=row["name"],
                description=row["description"],
                phone=row["phone"] or None,
                website=row["website"] or None,
                address=row["address"] or None,
                website_working=row["website_working"] == "True",
                social_links=[
                    link.strip()
                    for link in row["social_links"].split(",")
                    if link.strip()
                ],
                score=int(row["score"]),
                latitude=float(row["latitude"]) if row["latitude"] else None,
                longitude=float(row["longitude"]) if row["longitude"] else None,

            )
            leads.append(lead)
    return leads

