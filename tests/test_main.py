import pytest
from pricestat.main import load_csv_calc_keystats

def test_load_csv_calc_keystats():
    # test loading a sample csv file 'tests\GOOG_1Y.csv' and calculating avg/min/max
    assert load_csv_calc_keystats('tests\GOOG_1Y.csv') == [152.59, 123.40, 192.66]
