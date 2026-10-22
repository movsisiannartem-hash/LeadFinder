def normalize_text(value):
    if value is None:
        return None
    else:
        text_no_space = value.strip()
    return text_no_space


def normalize_name(value):
    normalized_name = " ".join(value.split()).title()
    return normalized_name

def normalize_phone(value):
    if value is None:
        return None

    normalized_phone = value.replace("(", "").replace(")", "").replace(" ", "").replace("-", "")
    if normalized_phone.startswith("8"):
        normalized_phone = "+7" + normalized_phone[1:]

    return normalized_phone

def normalize_website(value):
    if value is None:
        return None

    normalized_website = value.strip()
    if normalized_website.startswith("https://") or normalized_website.startswith("http://"):
        if normalized_website.endswith("/"):
            normalized_website = normalized_website[:-1]
    return normalized_website

def normalize_lead(lead):
    lead.name = normalize_name(lead.name)
    lead.description = normalize_text(lead.description)
    lead.phone = normalize_phone(lead.phone)
    lead.website = normalize_website(lead.website)

    return lead


if __name__ == "__main__":
    print(normalize_name("   beauty house   "))
    print(normalize_phone("8 (999) 123-45-67"))
    print(normalize_phone(None))
    print(normalize_website(" https://example.ru/ "))
    print(normalize_website(None))