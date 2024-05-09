import os

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


import os
import csv

import os
import csv

if __name__ == '__main__':
    folder_path = 'yamls/'
    csv_file_path = 'jogadores_base.csv'

    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Nome', 'Estrela', 'Pais', 'Time', 'Idade', 'Posicao', 'Titular', 'Top Mundial', 'Lado', 'Caracteristica 1', 'Caracteristica 2', 'Extra'])

        for filename in os.listdir(folder_path):
            if filename.endswith('.yml'):
                team_file_path = os.path.join(folder_path, filename)
                team_data = read_yaml(team_file_path)
                jogadores_base = get_base_info(team_data)
                for jogador in jogadores_base:
                    caracteristica_1 = jogador.caracteristicas[0] if jogador.caracteristicas else None
                    caracteristica_2 = jogador.caracteristicas[1] if len(jogador.caracteristicas) > 1 else None
                    csv_writer.writerow([jogador.nome, jogador.estrela, jogador.pais, jogador.time, jogador.idade, jogador.posicao, jogador.titular, jogador.top_mundial, jogador.lado, caracteristica_1, caracteristica_2, jogador.extra])

