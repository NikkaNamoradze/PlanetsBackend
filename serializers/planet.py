def decode_planet(planet) -> dict:
    return {
        "_id": str(planet["_id"]),
        "name": planet["name"],
        "description": planet["description"],
        "mass": planet["mass"],
        "diameter": planet["diameter"],
        "orbit_period": planet["orbit_period"],
        "day_length": planet["day_length"],
        "surface_temperature": planet["surface_temperature"],
        "atmosphere": planet["atmosphere"],
        "moons": planet["moons"],
        "notable_features": planet["notable_features"],
        "exploration": planet["exploration"],
        "trivia": planet["trivia"],
        "historical_significance": planet["historical_significance"],
        "from_sun": planet.get("from_sun"),
        "images": planet.get("images", [])
    }


def decode_planets(planets) -> list:
    return [decode_planet(doc) for doc in planets]
