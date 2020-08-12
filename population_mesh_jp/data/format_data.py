from typing import Dict
import luigi
import numpy as np

from population_mesh_jp.utils.task_template import PopulationMeshJP
from population_mesh_jp.data.download_json import DownloadJsonData


class FormatToArray(PopulationMeshJP):
    map_id: str = luigi.Parameter()
    year: str = luigi.Parameter()

    def requires(self):
        return DownloadJsonData(map_id=self.map_id, year=self.year)

    def run(self):
        data = self.load()
        array_data = self._make_array(data=data)
        self.dump(array_data)

    @classmethod
    def _make_array(cls, data: list):
        array_data = np.ones((8 * 10 * 2, 8 * 10 * 2)) * -9999

        for single_data in data['GET_STATS_DATA']['STATISTICAL_DATA']['DATA_INF']['VALUE']:
            row_number, col_number, value = cls._decompose_item(single_data=single_data)
            array_data[row_number, col_number] = value

        return np.flipud(array_data.astype(np.int32))

    @staticmethod
    def _decompose_item(single_data: dict):
        area = single_data['@area']
        value = int(single_data['$'])

        row_number = (20 * int(area[4:5])) + (2 * int(area[6:7])) + ((int(area[8]) - 1) // 2)
        col_number = (20 * int(area[5:6])) + (2 * int(area[7:8])) + ((int(area[8]) - 1) % 2)

        return row_number, col_number, value
