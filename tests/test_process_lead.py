
from utils.processor import process_lead
from models import Lead


def test_process_lead():
    lead = Lead(
        name="fff",
        website=None,
        phone="484884",
        social_links=["httpsjjf.com"]
    )

    processed_lead, priority = process_lead(lead)

    assert processed_lead.score == 7
    assert priority == "HOT"
