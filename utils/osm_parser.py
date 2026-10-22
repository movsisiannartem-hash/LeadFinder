from models import Lead

def parse_osm(data):
    leads = []


    elements = data.get("elements", [])
    if not isinstance(elements, list):
        return leads

    for item in elements:
        social_links = []

        addr_parts = []

        tags = item.get("tags", {})
        name = tags.get("name")
        description = tags.get("description")
        phone = tags.get("phone") or tags.get("contact:phone")
        website = tags.get("website") or tags.get("contact:website")


        if tags.get("contact:instagram"):
            social_links.append(tags.get("contact:instagram"))
        if tags.get("contact:vk"):
            social_links.append(tags.get("contact:vk"))
        if tags.get("contact:telegram"):
            social_links.append(tags.get("contact:telegram"))
        if tags.get("contact:whatsapp"):
            social_links.append(tags.get("contact:whatsapp"))
        if tags.get("contact:max"):
            social_links.append(tags.get("contact:max"))

        if tags.get("addr:city"):
            addr_parts.append(tags.get("addr:city"))
        if tags.get("addr:street"):
            addr_parts.append(tags.get("addr:street"))
        if tags.get("addr:housenumber"):
            addr_parts.append(tags.get("addr:housenumber"))
        address = ", ".join(addr_parts)


        if not name:
            continue

        lead = Lead(
            name=name,
            description=description,
            phone=phone,
            website=website,
            social_links=social_links,
            address=address,
            latitude=item.get("lat") or item.get("center", {}).get("lat"),
            longitude=item.get("lon") or item.get("center", {}).get("lon"),
        )
        leads.append(lead)

    return leads
