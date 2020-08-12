import luigi
import numpy as np
import gokart

import population_mesh_jp

if __name__ == '__main__':
    assert luigi.configuration.add_config_path('./conf/param.ini')
    assert luigi.configuration.add_config_path('./conf/run_settings.ini')
    np.random.seed(57)
    gokart.run()
