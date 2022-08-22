import subprocess


def red(text):
    return "\033[31m{}\033[00m".format(text)


if __name__ == "__main__":
    for file in [
            "~/.gitconfig", "~/.gitignore_global", "~/.hyper.js", "~/.tigrc"
    ]:
        subprocess.run("cp {} .".format(file), shell=True, check=True)
        print("{} copied".format(red(file)))
