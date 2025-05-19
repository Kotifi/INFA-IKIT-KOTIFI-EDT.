import unittest
from meter import METER_TYPE, ColdWaterMeter, HotWaterMeter
from model import Model


class TestMeterClasses(unittest.TestCase):
    def test_meter_paramsda_date(self):
        cold = ColdWaterMeter("2023-01-01", 100)
        self.assertEqual(cold.get_params()['date'], "2023-01-01")
    def test_meter_params_value(self):
        cold = ColdWaterMeter("2023-01-01", 100)
        self.assertEqual(cold.get_params()['value'], 100)
    def test_meter_params_type(self):
        cold = ColdWaterMeter("2023-01-01", 100)
        self.assertEqual(cold.get_params()['type'], 'cold_water')

class TestMETER_TYPE(unittest.TestCase):
    def test_get_type_on_nameC(self):
        self.assertEqual(METER_TYPE.get_type_on_name('Счетчик холодной воды'), METER_TYPE.COLD_WATER)
    def test_get_type_on_nameH(self):
        self.assertEqual(METER_TYPE.get_type_on_name('Счетчик горячей воды'), METER_TYPE.HOT_WATER)
    def test_get_type_on_nameE(self):
        self.assertEqual(METER_TYPE.get_type_on_name('Счетчик электричества'), METER_TYPE.ELECTRICITY)
    def test_get_type_on_nameU(self):
        self.assertIsNone(METER_TYPE.get_type_on_name('unknown_type'))

class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = Model()
        
    def test_create_and_remove1(self):
        id1 = self.model.create(METER_TYPE.COLD_WATER, "2023-01-01", 100)
        id2 = self.model.create(METER_TYPE.HOT_WATER, "2023-01-02", 50)
        
        self.assertEqual(len(self.model.select_all()), 2)

    def test_create_and_remove2(self):
        id1 = self.model.create(METER_TYPE.COLD_WATER, "2023-01-01", 100)
        id2 = self.model.create(METER_TYPE.HOT_WATER, "2023-01-02", 50)

        self.assertIsInstance(self.model.select_all()[id1], ColdWaterMeter)

    def test_create_and_remove3(self):
        id1 = self.model.create(METER_TYPE.COLD_WATER, "2023-01-01", 100)
        id2 = self.model.create(METER_TYPE.HOT_WATER, "2023-01-02", 50)

        self.assertIsInstance(self.model.select_all()[id2], HotWaterMeter)
        
    def test_create_and_remove4(self):
        id1 = self.model.create(METER_TYPE.COLD_WATER, "2023-01-01", 100)
        id2 = self.model.create(METER_TYPE.HOT_WATER, "2023-01-02", 50)

        self.model.remove(id1)

        self.assertEqual(len(self.model.select_all()), 1)

    def test_create_and_remove5(self):
        id1 = self.model.create(METER_TYPE.COLD_WATER, "2023-01-01", 100)
        id2 = self.model.create(METER_TYPE.HOT_WATER, "2023-01-02", 50)

        self.model.remove(id1)

        self.assertNotIn(id1, self.model.select_all().keys())
        
    def test_id_increment(self):
        id1 = self.model.create(METER_TYPE.COLD_WATER, "2023-01-01", 100)
        id2 = self.model.create(METER_TYPE.HOT_WATER, "2023-01-02", 50)
        self.assertEqual(id1 + 1, id2)



if __name__ == '__main__':
    unittest.main()