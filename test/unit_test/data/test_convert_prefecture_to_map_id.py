import unittest

from population_mesh_jp.data.map_id_converter import build_map_id_list, convert_prefecture_to_mapid_list, convert_prefecture_to_latlon, lat2id, lon2id


class TestConvertPrefectureToLatlon(unittest.TestCase):
    def test_build_map_id_list(self):
        resulted = build_map_id_list(prefecture_name_list=['神奈川'])
        self.assertEqual(resulted, ['5238', '5239', '5338', '5339'])

    def test_convert_prefecture_to_mapid_list(self):
        resulted = convert_prefecture_to_mapid_list(prefecture_name='神奈川')
        self.assertEqual(resulted, ['5238', '5239', '5338', '5339'])

    def test_convert_prefecture_to_latlon(self):
        resulted = convert_prefecture_to_latlon(prefecture_name='北海道')
        expected = (41.35194444444445, 45.55722222222222, 139.33444444444444, 148.89305555555555)
        self.assertAlmostEqual(resulted[0], expected[0])
        self.assertAlmostEqual(resulted[1], expected[1])
        self.assertAlmostEqual(resulted[2], expected[2])
        self.assertAlmostEqual(resulted[3], expected[3])

    def test_lat2id(self):
        self.assertEqual(lat2id(lat=36.1), 54)
        self.assertEqual(lat2id(lat=43.9), 65)

    def test_lon2id(self):
        self.assertEqual(lon2id(lon=134.1), 34)
        self.assertEqual(lon2id(lon=138.9), 38)
