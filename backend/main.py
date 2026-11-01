from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from calculations.resistance import vertical_rod_resistance
app = FastAPI(title="GroundStudio API", version="0.1.0", description="Preliminary prototype; not certified for final design.")
class RodRequest(BaseModel):
    soil_resistivity: float = Field(gt=0, description="ohm-m")
    length_m: float = Field(gt=0, description="metres")
    diameter_mm: float = Field(gt=0, description="millimetres")
@app.get("/")
def root(): return {"name":"GroundStudio API","version":"0.1.0","status":"prototype"}
@app.get("/health")
def health(): return {"status":"ok"}
@app.post("/calculations/vertical-rod")
def calculate_vertical_rod(req: RodRequest):
    try: value=vertical_rod_resistance(req.soil_resistivity,req.length_m,req.diameter_mm/1000)
    except ValueError as exc: raise HTTPException(status_code=422,detail=str(exc)) from exc
    return {"estimate_ohm":value,"status":"preliminary_estimate","warning":"Single vertical rod in homogeneous soil only; not group resistance or a safety study."}
