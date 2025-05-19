import pytest
from pytest_check import check
from meter import METER_TYPE, ColdWaterMeter, HotWaterMeter, ElectricityMeter
from model import Model

class TestMeterClasses:
    def test_meter_params(self):
        cold = ColdWaterMeter("2023-01-01", 100)
        with check:
            assert cold.get_params()['date'] == "2023-01-01"
            assert cold.get_params()['value'] == 100
            assert cold.get_params()['type'] == 'cold_water'

class TestMETER_TYPE:
    def test_get_type_on_name(self):
        with check:
            assert METER_TYPE.get_type_on_name('Счетчик холодной воды') == METER_TYPE.COLD_WATER
            assert METER_TYPE.get_type_on_name('cold_water') == METER_TYPE.COLD_WATER
            assert METER_TYPE.get_type_on_name('Счетчик горячей воды') == METER_TYPE.HOT_WATER
            assert METER_TYPE.get_type_on_name('ghot_water') == METER_TYPE.HOT_WATER #g
            assert METER_TYPE.get_type_on_name('Счетчик электричества') == METER_TYPE.ELECTRICITY
            assert METER_TYPE.get_type_on_name('gelectricity') == METER_TYPE.ELECTRICITY #g
            assert METER_TYPE.get_type_on_name('unknown_type') is None