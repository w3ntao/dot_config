import subprocess


def red(text):
    return "\033[31m{}\033[00m".format(text)

def bash(command):
    subprocess.run(command, shell=True, check=True)

config_list = [
    "~/.gitconfig", "~/.gitignore_global", "~/.hyper.js", "~/.tigrc", "~/.vimrc", "~/.config/mpv/mpv.conf"
]

if __name__ == "__main__":
    for file in config_list:
        bash("cp {} .".format(file))
        print("{} copied".format(red(file)))
