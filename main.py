import yaml
from models import TeamModel as Time
from models import PlayerModel as Jogador


def read_yaml(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        team_data = yaml.safe_load(file)
    return team_data


def get_team_info(team_file_path):
    try:
        team_data = read_yaml(team_file_path)
    except FileNotFoundError:
        print(f'Arquivo {team_file_path} não encontrado.')
        exit(1)
    except Exception as e:
        print(f'Erro desconhecido em ler o arquivo: {e}')
        exit(1)
    pass

    return team_data


def get_base_info(team_data):
    try:
        jogadores_base_info = [Jogador.Jogador(**jogador) for jogador in team_data['jogadores_base']]
    except KeyError:
        print('Erro ao carregar jogadores base.')
        exit(1)
    except Exception as e:
        print(f'Erro desconhecido em pegar jogadores da base: {e}')
        exit(1)

    for jogador in jogadores_base_info:
        jogador.dict()
        jogador.time = team_data['nome']
        print(jogador.dict())

    return jogadores_base_info


if __name__ == '__main__':
    team_file_path = 'teamsyamls/academia_ven.yml'

    team_infos = get_team_info(team_file_path)
    jogadores_base = get_base_info(team_infos)
