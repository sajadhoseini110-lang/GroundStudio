import math
def vertical_rod_resistance(soil_resistivity: float, length_m: float, diameter_m: float) -> float:
    """Simplified single vertical rod estimate in homogeneous soil. Validate equation and assumptions against the governing reference before engineering use."""
    if soil_resistivity<=0: raise ValueError("Soil resistivity must be greater than zero.")
    if length_m<=0 or diameter_m<=0: raise ValueError("Length and diameter must be greater than zero.")
    if diameter_m>=length_m: raise ValueError("Rod diameter must be smaller than rod length.")
    value=(soil_resistivity/(2*math.pi*length_m))*(math.log(4*length_m/diameter_m)-1)
    if value<=0 or not math.isfinite(value): raise ValueError("Inputs produced a non-physical result.")
    return value
