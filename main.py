import json
from storage import csv_storage, json_storage
from utils.filters import filter_leads
from utils.processor import process_lead
from utils.osm_parser import parse_osm
from utils.osm_query import build_query
from utils.cities import CITIES
from utils.deduplicator import remove_duplicates
from utils.niches import NICHE_TAGS
from utils.website_checker import check_websites
from utils.normalizer import normalize_lead
from utils.source_client import fetch_data
from utils.source_selector import choose_source
from utils.logger import setup_logger


def main():
    logger = setup_logger()
    logger.info("LeadFinder запущен")

    city = input("Введите город: ").strip().title()
    niche = input("Введите нишу: ").strip().lower()

    source = choose_source()
    if source is None:
        print("Неверный выбор источника")
        return

    if source == "2gis":
        print("2GIS пока не подключён")
        return

    if city not in CITIES:
        print("Неизвестный город")
        return

    if niche not in NICHE_TAGS:
        print("Неизвестная ниша")
        return

    tag, value = NICHE_TAGS[niche]

    coordinates = CITIES[city]
    south, west, north, east = coordinates

    query = build_query(tag, value, south, west, north, east)

    response = fetch_data(source, query)

    if response is None:
        return

    try:
        data = response.json()
        if not isinstance((data.get("elements")), list):
            print("Сервер вернул некорректные данные")
            return
        if not data.get("elements"):
            print("Компании не найдены")
            return
    except json.decoder.JSONDecodeError:
        print("Сервер вернул некорректный json")
        return



    leads = parse_osm(data)
    if not leads:
        print("Не удалосб найти подходящие компании")
        return


    leads = remove_duplicates(leads)

    for lead in leads:
        normalize_lead(lead)



    leads_with_website = [lead for lead in leads if lead.website]
    urls = [lead.website for lead in leads_with_website]
    results = check_websites(urls)


    for lead_with_website, result in zip(leads_with_website, results):
        lead_with_website.website_working = result


    for lead in leads:
        if not lead.website:
            lead.website_working = False

    for lead in leads:
        process_lead(lead)








    sorted_leads = sorted(
        leads,
        key=lambda lead: lead.score,
        reverse=True
    )

    print("Лиды по приоритету:")

    good_leads = filter_leads(sorted_leads, 2)

    print("Хорошие лиды:")

    for lead in good_leads:
        print(f"{lead.name} — score: {lead.score}")

    csv_storage.save_leads_to_csv(good_leads, "data/leads.csv")
    json_storage.save_leads_to_json(good_leads, "data/leads.json")





if __name__ == "__main__":
    main()

