import yaml

from models import TeamModel as Time
from models import EstadioModel as Estadio


def read_yaml():
    with open('teamsyamls/academia_ven.yml', 'r', encoding="utf-8") as file:
        file = yaml.safe_load(file)
        return file


def get_team_info(team):
    time = Time.Time(**team)


if __name__ == '__main__':
    team = read_yaml()
    infos_team = get_team_info(team)
