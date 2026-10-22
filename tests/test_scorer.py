from utils.scorer import calculate_score
from models import Lead

lead1 = Lead(
    name="Beauty Salon",
    website=None,
    phone="+79991234567",
    social_links=["https://t.me/salon"]


)

lead2 = Lead(
    name="vnnv",
    website="https://vnn.com",
    phone="+79991234567",
    social_links=["https://t.me/salon"],
    website_working=True
)

lead3 = Lead(
    name="fff",
    website=None,
    phone=None,
    social_links=[]

)

def test_lead_score():

    if lead1.website is None and lead1.phone and len(lead1.social_links) >= 1:
        assert calculate_score(lead1) == 7

def test_lead_score2():
    if lead2.website and lead2.website_working and len(lead2.social_links) >= 1 and lead2.phone:
        assert calculate_score(lead2) == 2

def test_lead_score3():
    if not lead3.website and len(lead3.social_links) == 0 and not lead3.phone:
        assert calculate_score(lead3) == 5