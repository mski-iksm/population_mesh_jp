import luigi
import numpy as np
import gokart

import population_mesh_jp

if __name__ == '__main__':
    luigi.configuration.LuigiConfigParser.add_config_path('./conf/param.ini')
    np.random.seed(57)
    gokart.run()
