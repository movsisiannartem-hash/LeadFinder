from models import Lead
from utils.deduplicator import remove_duplicates
lead1 = Lead(
    name="fff",
    address="ff",
)

lead2 = Lead(
    name="fff",
    address="ff",
)



def test_remove_duplicates():
    assert remove_duplicates([lead1, lead2]) == [lead1]