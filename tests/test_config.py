
import pytest
from utils.config import load_config


def test_load_config_valid(monkeypatch):
    monkeypatch.setenv("REQUEST_TIMEOUT", "30")
    monkeypatch.setenv("MAX_WORKERS", "20")

    config = load_config()

    assert config["request_timeout"] == 30
    assert config["max_workers"] == 20


def test_load_config_invalid_timeout(monkeypatch):
    monkeypatch.setenv("REQUEST_TIMEOUT", "-5")
    monkeypatch.setenv("MAX_WORKERS", "20")

    with pytest.raises(ValueError):
        load_config()


def test_load_config_invalid_workers(monkeypatch):
    monkeypatch.setenv("REQUEST_TIMEOUT", "30")
    monkeypatch.setenv("MAX_WORKERS", "0")

    with pytest.raises(ValueError):
        load_config()

#67