from typing import List, Optional
from pydantic import BaseModel


class PlanetModel(BaseModel):
    name: str
    description: str
    mass: str
    diameter: str
    orbit_period: str
    day_length: str
    surface_temperature: str
    atmosphere: str
    moons: str
    notable_features: List[str]
    exploration: List[str]
    trivia: List[str]
    historical_significance: str
    from_sun: Optional[int]
    images: List[str]
