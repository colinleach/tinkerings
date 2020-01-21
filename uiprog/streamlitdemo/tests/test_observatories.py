import astropy.units as u
from astropy.units import Unit

from pytest import approx

from streamlitdemo import observatories 

obs = observatories.Observatories()

def test_init():
    assert obs.df.shape == (38, 4)
    expected_regions = ['NorthAmerica', 'SouthAmerica', 'Australia', 'EuropeMed', 'Asia', 'Africa']
    assert obs.regions == expected_regions
    assert len(obs.loc) == 38
    assert obs.loc['ALMA'].unit == Unit("m")

def test_show_loc():
    obs.curr_site = 'ALMA'
    obs.show_loc()
    assert obs.observing_location.height.value == approx(5000.)