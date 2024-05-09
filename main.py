import yaml


def read_yaml():
    with open('teamsyamls/academia_ven.yml', 'r', encoding="utf-8") as file:
        files = yaml.safe_load(file)
        print(files)


if __name__ == '__main__':
    read_yaml()
