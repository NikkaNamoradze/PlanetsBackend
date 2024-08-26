from fastapi import APIRouter, HTTPException
from config.config import planets_collection
from models.planet import PlanetModel
from serializers.planet import decode_planet, decode_planets
from bson import ObjectId
import datetime

planet_root = APIRouter()


@planet_root.post("/new/planet")
def new_planet(planet: PlanetModel):
    doc = dict(planet)
    current_date = datetime.date.today()
    doc["date"] = str(current_date)

    res = planets_collection.insert_one(doc)

    doc_id = str(res.inserted_id)

    return {
        "status": "ok",
        "message": "Planet added successfully",
        "_id": doc_id
    }


@planet_root.get("/all_planets")
def all_planets():
    res = planets_collection.aggregate([
        {
            "$addFields": {
                "from_sun_sort": {"$ifNull": ["$from_sun", float('inf')]}
            }
        },
        {
            "$sort": {"from_sun_sort": 1}
        }
    ])

    decoded_data = decode_planets(res)

    return {
        "status": "ok",
        "data": decoded_data
    }


@planet_root.get("/planet/{_id}")
def get_planet(_id: str):
    res = planets_collection.find_one({"_id": ObjectId(_id)})
    if res:
        decoded_planet = decode_planet(res)
        return {
            "status": "ok",
            "data": decoded_planet
        }
    else:
        raise HTTPException(status_code=404, detail="Planet not found")


@planet_root.put("/planet/{_id}")
def update_planet(_id: str, updated_data: PlanetModel):
    update_result = planets_collection.update_one(
        {"_id": ObjectId(_id)},
        {"$set": updated_data.dict()}
    )

    if update_result.modified_count == 1:
        updated_planet = planets_collection.find_one({"_id": ObjectId(_id)})
        return {
            "status": "ok",
            "message": "Planet updated successfully",
            "data": decode_planet(updated_planet)
        }
    else:
        raise HTTPException(status_code=404, detail="Planet not found or no changes made")


@planet_root.delete("/delete_all_planets")
def delete_all_planets():
    delete_result = planets_collection.delete_many({})

    if delete_result.deleted_count > 0:
        return {
            "status": "ok",
            "message": f"All planets deleted successfully. Total deleted: {delete_result.deleted_count}"
        }
    else:
        return {
            "status": "ok",
            "message": "No planets found to delete."
        }
