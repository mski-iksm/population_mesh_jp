import os
import subprocess
import luigi

if __name__ == '__main__':
    os.environ['MODEL_PATH'] = './conf/run_settings.ini'

    command = ['python', 'main.py', 'population_mesh_jp.RunDownload', '--local-scheduler']

    subprocess.call(command)
