from fastapi import FastAPI
from .models.machine import Machine
from .data.machines import machine_list


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API de serviços de máquinas"}

@app.get("/machines/")
async def read_machines():
    return machine_list

@app.get("/machines/{machine_id}")
async def read_machine(machine_id: int):
    return (machine for machine in machine_list if machine["id"] == machine_id)

@app.post("/machines/")
async def create_machine(machine: Machine):
    machine_list.append(machine)
    return machine

@app.put("/machines/{machine_id}")
async def update_machine(machine_id: int, machine: Machine):
    return {"machine_name": machine.name, "machine_id": machine_id}

@app.delete("/machines/{machine_id}")
async def delete_machine(machine_id: int):
    return {"machine_id": machine_id}