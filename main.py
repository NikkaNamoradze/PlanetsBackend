from fastapi import FastAPI
from routes.entry import entry_root
from routes.planet import planet_root

app = FastAPI()

app.include_router(entry_root)
app.include_router(planet_root)
