#pip install fastapi
#pip install uvicorn

#uvicorn main:app --reload
from fastapi import FastAPI ,Path
from typing import  Optional
from pydantic import  BaseModel


app=FastAPI()
class Item(BaseModel):
    name:str
    price:float
    brand:Optional[str]="Regular"
class UpdateItem(BaseModel):
    name:Optional[str]=None
    price:Optional[float]=None
    brand:Optional[str]=None


inventory={
    1:{
        "name":"Milk",
        "price":25,
        "brand":"Regular"
    },
2:{
        "name":"Coconut",
        "price":40,
        "brand":"Regular"
    }
}

@app.get("/get-item/{item_id}")
def get_item_by_id(item_id:int=Path(description="The ID of the Product you want to view",ge=0)):
    return inventory[item_id]

@app.get("/get-item-by-name")
def about(name:Optional[str]):
    for item_id in inventory:
        if inventory[item_id]["name"]==name:
            return inventory[item_id]
    return {"Data":"Not Found"}


@app.post("/create-item/{item_id}")
def post_inventory(item_id:int,item:Item):
    if item_id in inventory:
        return {"Error":f"Item id {item_id} already exists"}
    else:
        inventory[item_id]=item
        return inventory[item_id]

@app.patch("/update-item/{item_id}")
def post_inventory(item_id:int,item:UpdateItem):
    if item_id not in inventory:
        return {"Error":f"Item id {item_id} does not exists"}
    else:
        if item.name !=None:
            inventory[item_id]["name"]=item.name
        if item.price!=None:
            inventory[item_id]["price"]=item.price
        if item.brand!=None:
            inventory[item_id]["brand"]=item.brand
        return inventory[item_id]


@app.delete("/delete-item/{item_id}")
def delete_inventory(item_id:int):
    if item_id not in inventory:
        return {"Error":f"Item id {item_id} does not exists"}
    else:
        del inventory[item_id]
        return {"Message": f"Item id {item_id} deleted successfully"}