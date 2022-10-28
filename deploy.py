import subprocess
from glob import glob
from os import path
from collect import config_list, red

if __name__ == "__main__":
    for file_full_path in config_list:
        file_local = path.basename(file_full_path)
        subprocess.run("sudo cp {} {}".format(file_local, file_full_path),
                       shell=True,
                       check=True)
        print("{} deployed".format(red(file_local)))
