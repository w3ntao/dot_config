import subprocess


def red(text):
    return "\033[31m{}\033[00m".format(text)


config_list = [
    "~/.gitconfig", "~/.gitignore_global", "~/.hyper.js", "~/.tigrc", "~/.vimrc"
]

if __name__ == "__main__":
    for file in config_list:
        subprocess.run("cp {} .".format(file), shell=True, check=True)
        print("{} copied".format(red(file)))

