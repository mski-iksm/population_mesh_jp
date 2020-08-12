import unittest

from population_mesh_jp.data.download_json import DownloadJsonData


class TestDownloadJsonData(unittest.TestCase):
    def test_donwload_json(self):
        downloaded_data = DownloadJsonData._download_json(app_id='980b1072c2da779c8905f05ff8fe1c0b1fcb9949',
                                                          map_id='5437',
                                                          year='2010')
