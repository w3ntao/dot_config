import subprocess
from glob import glob
from os import path
from collect import bash, config_list, red

if __name__ == "__main__":
    for file_full_path in config_list:
        file_local = path.basename(file_full_path)

        bash("mkdir -p {}".format(path.dirname(file_full_path)))
        bash("cp {} {}".format(file_local, file_full_path))
        print("{} deployed".format(red(file_local)))
