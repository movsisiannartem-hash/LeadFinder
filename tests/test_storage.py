
import json

from models import Lead
from storage.csv_storage import save_leads_to_csv, load_leads_from_csv
from storage.json_storage import save_leads_to_json, load_leads_from_json


def test_json_storage(tmp_path):
    leads = [
        Lead(name="Salon A", phone="+79991234567", score=7),
        Lead(name="Salon B", website="https://example.com", score=3),
    ]

    file_path = tmp_path / "leads.json"
    save_leads_to_json(leads, file_path)
    loaded_leads = load_leads_from_json(file_path)

    assert len(loaded_leads) == 2
    assert loaded_leads[0].name == "Salon A"
    assert loaded_leads[0].score == 7


def test_csv_storage(tmp_path):
    leads = [
        Lead(name="Salon A", phone="+79991234567", score=7),
        Lead(name="Salon B", website="https://example.com", score=3),
    ]

    file_path = tmp_path / "leads.csv"
    save_leads_to_csv(leads, file_path)
    loaded_leads = load_leads_from_csv(file_path)

    assert len(loaded_leads) == 2
    assert loaded_leads[0].name == "Salon A"
    assert loaded_leads[0].score == 7
