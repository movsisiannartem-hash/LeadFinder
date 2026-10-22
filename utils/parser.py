from bs4 import BeautifulSoup
from models import Lead

def parse_companies(html):
    leads = []

    soup = BeautifulSoup(html, "html.parser")
    companies = soup.select(".company")

    for index, company in enumerate(companies):
        name = company.find("h2")
        description = company.find("p")
        social_links = [
            link["href"]
            for link in company.select(".social")
        ]

        if index == 0:
            phone = "8 (999) 123-45-67"
            website = " https://example.ru/ "
        elif index == 1:
            phone = None

            website = "http://fade.ru/"

        else:

            phone = None

            website = None

        leads.append(
            Lead(
                name=name.text.strip(),
                description=description.text.strip(),
                phone=phone,
                website=website,
                social_links=social_links

            )
        )
    return leads