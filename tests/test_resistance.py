import math, pytest
from backend.calculations.resistance import vertical_rod_resistance
def test_positive_finite_result():
    result=vertical_rod_resistance(350,2.4,0.016)
    assert result>0 and math.isfinite(result)
def test_zero_resistivity_rejected():
    with pytest.raises(ValueError): vertical_rod_resistance(0,2.4,0.016)
def test_invalid_geometry_rejected():
    with pytest.raises(ValueError): vertical_rod_resistance(350,0.01,0.016)
