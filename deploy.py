import subprocess
from glob import glob
from os import path

from collect import red

if __name__ == "__main__":
    for file in glob(".*"):
        if path.isdir(file):
            continue

        subprocess.run("cp {} ~/".format(file), shell=True, check=True)
        print("{} deployed".format(red(file)))
