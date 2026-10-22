def calculate_score(lead):
    score = 0
    if lead.website is None:
        score += 5
    if lead.website and not lead.website_working:
        score += 3
    if lead.phone:
        score += 1
    if len(lead.social_links) >= 1:
        score += 1
    return score


