import itertools

teams = [
    'Corinthians', 'Palmeiras', 'Vasco da Gama', 'América-MG', 'Athletico-PR',
    'Atlético-MG', 'Bahia', 'Botafogo', 'Vitória', 'Cruzeiro', 'Cuiabá',
    'Flamengo', 'Fluminense', 'Fortaleza', 'Juventude', 'Grêmio', 'Internacional', 'RB Bragantino', 'Criciúma', 'São Paulo'
]

matches = list(itertools.combinations(teams, 2))

for match in matches:
    print(f'("{match[0]}", "{match[1]}"),')
    print(f'("{match[1]}", "{match[0]}"),')



