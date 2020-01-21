import numpy as np
import astropy.units as u
from astropy.units import Unit

from pytest import approx

from streamlitdemo import redshifts 

rs = redshifts.Redshifts()

def test_init():
    # currently 6 cosmologies, astropy may change this in future
    cosm_count = len(rs.cosmologies)
    assert cosm_count >= 6
    assert rs.df.shape[0] == 200
    assert rs.df.shape[1] == cosm_count + 1
    assert rs.df_long.shape[0] == 200 * cosm_count
    assert rs.df_long.shape[1] == 3

def test_calc_angular_diameter():
    dist, ages, ageticks = rs.calc_angular_diameter()
    assert len(dist) == 200
    expected_ages = np.array([13., 10.,  8.,  6.,  5.,  4.,  3.,  2.,  1.5,  1.2, 1.])
    assert len(ages) == len(expected_ages)
    assert not (ages.value - expected_ages).any()
    assert len(ageticks) == len(expected_ages)
