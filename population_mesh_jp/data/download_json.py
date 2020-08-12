from typing import Tuple

import luigi
import requests

from population_mesh_jp.utils.task_template import PopulationMeshJP


class DownloadJsonData(PopulationMeshJP):
    app_id: str = luigi.Parameter()
    map_id: str = luigi.Parameter()
    year: str = luigi.Parameter()

    def run(self):
        response_json = self._download_json(app_id=self.app_id, map_id=self.map_id, year=self.year)
        self.dump(response_json)

    @classmethod
    def _download_json(cls, app_id: str, map_id: str, year: str):
        baseurl = 'https://api.e-stat.go.jp/rest/2.1/app/json/getStatsData?'

        table_id = cls._get_table_id(year=year)
        statsdataid = f'{table_id}M{map_id}'
        payloads = cls._get_payloads(appId=app_id, statsDataId=statsdataid)
        response = requests.get(baseurl, params=payloads)

        if response.status_code != 200:
            raise requests.exceptions.HTTPError('status_code is not 200')

        response_json = response.json()

        return response_json

    @staticmethod
    def _get_table_id(year):
        if year == '2015':
            return 'T000847'
        if year == '2010':
            return 'T000609'
        if year == '2005':
            return 'T000387'
        if year == '2000':
            return 'T000386'
        if year == '1995':
            return 'T000752'
        raise ValueError(f'year={year} is not in 2015, 2010, 2005, 2000, 1995')

    @staticmethod
    def _get_payloads(**kwargs):
        return kwargs
