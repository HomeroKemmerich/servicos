from fastapi import FastAPI
from .models.machine import Machine



app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API de serviços de máquinas"}

@app.get("/items/")
async def read_items():
    return []

@app.get("/items/{machine_id}")
async def read_item(machine_id: int):
    return {"item_id": machine_id}

@app.post("/items/")
async def create_item(machine: Machine):
    return machine

@app.put("/items/{machine_id}")
async def update_item(machine_id: int, machine: Machine):
    return {"item_name": machine.name, "item_id": machine_id}

@app.delete("/items/{machine_id}")
async def delete_item(machine_id: int):
    return {"item_id": machine_id}