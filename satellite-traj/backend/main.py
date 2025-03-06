from fastapi import FastAPI
from pydantic import BaseModel
from your_trajectory_module import calculate_trajectory  # Import your Python function

app = FastAPI()

class TrajectoryInput(BaseModel):
    planet: str
    altitude: float
    velocity: float

@app.post("/calculate-trajectory")
async def get_trajectory(data: TrajectoryInput):
    result = calculate_trajectory(data.planet, data.altitude, data.velocity)
    return {"trajectory": result}