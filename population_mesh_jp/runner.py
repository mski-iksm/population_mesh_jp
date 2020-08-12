from typing import Tuple
import itertools

import luigi

from population_mesh_jp.utils.task_template import PopulationMeshJP
from population_mesh_jp.data.map_id_converter import build_map_id_list
from population_mesh_jp.data.format_data import FormatToArray


class RunDownload(PopulationMeshJP):
    prefecture_name_list: Tuple[str] = luigi.ListParameter()
    year_list: Tuple[str] = luigi.ListParameter()

    def requires(self):
        map_id_list = build_map_id_list(prefecture_name_list=self.prefecture_name_list)
        map_id_year_pair = itertools.product(map_id_list, self.year_list)

        return {FormatToArray(map_id=map_id, year=year) for map_id, year in map_id_year_pair}

    def run(self):
        return self.dump('done')
