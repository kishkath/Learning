
from fastapi import FastAPI

app = FastAPI()

food_items = {
    'indian': ["samosa","Dosa"],
    'american': ['hot god','apple pie']
}

valid_cuisines = food_items.keys()
@app.get("/get_items/{cuisine}")
async def get_items(cuisine):
    return food_items.get(cuisine)


