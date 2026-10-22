from dataclasses import dataclass, field

@dataclass
class Lead:
    name: str
    description: str | None = None
    phone: str | None = None
    website: str | None = None
    address: str | None = None
    website_working: bool = False
    social_links: list[str] = field(default_factory=list)
    score: int = 0
    latitude: float | None = None
    longitude: float | None = None

