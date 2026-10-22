from utils.normalizer import normalize_name
from utils.normalizer import normalize_phone
from utils.normalizer import normalize_website

def test_normalize_name():
    assert normalize_name("   dolce  vita  ") == "Dolce Vita"

def test_normalize_name_uppercase():
    assert normalize_name("BARBER SHOP") == "Barber Shop"

def test_normalize_phone():
    assert normalize_phone(None) is None

def test_normalize_website1():
    assert normalize_website(None) is None

def test_normalize_website2():
    assert normalize_website(" https://example.com/") == "https://example.com"

def test_normalize_website3():
    assert normalize_website("https://example.com") == "https://example.com"


