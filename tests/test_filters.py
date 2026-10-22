
from models import Lead
from utils.filters import filter_leads


def test_filter_leads():
    leads = [
        Lead(name="Salon A", score=7),
        Lead(name="Salon B", score=3),
        Lead(name="Salon C", score=1),
    ]

    result = filter_leads(leads, min_score=3)

    assert len(result) == 2
    assert all(lead.score >= 3 for lead in result)
    assert result[0].name == "Salon A"
    assert result[1].name == "Salon B"
