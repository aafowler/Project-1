import pandas as pd

stats = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2025_per_game.html')

df = stats[0]

df.to_csv('nba_2025_stats.csv', index=False)


team_players = {}


for index, row in df.iterrows():
    team = row['Team']
    player = row['Player']
    if pd.notna(team) and pd.notna(player):
        if team not in team_players:
            team_players[team] = []
        team_players[team].append(player)

team_players_sorted = sorted(team_players)
