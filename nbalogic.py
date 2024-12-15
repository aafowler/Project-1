import pandas as pd

def get_data() -> pd.DataFrame:
    """

    Retrieves player stats from basketball-reference.com for the 2025 season,
    converts the data into a Pandas DataFrame, and saves it as a CSV file named 'nba_2025_stats.csv'.

    Returns:
        pandas.DataFrame: DataFrame that has all NBA player stats.
    """
    stats = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2025_per_game.html')
    df = stats[0]
    df.to_csv('nba_2025_stats.csv', index=False)
    return df

def get_players(df: pd.DataFrame) -> dict:
    """
    Creates a dictionary With teams as the key and players as the value.

    Handles missing team or player data.

    Args:
        df: DataFrame containing NBA player data.

    Returns:
        team_players: A dictionary connecting team names to lists of players on the team.
    """
    team_players = {}
    for index, row in df.iterrows():
        team = row['Team']
        player = row['Player']
        if pd.notna(team) and pd.notna(player):
            if team not in team_players:
                team_players[team] = []
            team_players[team].append(player)
    return team_players

def get_stats(df: pd.DataFrame, team: str, player: str) -> dict | None:
    """
    Gets the points, rebounds, and assists of selected player.

    Args:
        df: DataFrame containing NBA player stats.
        team (str): The name of the team.
        player (str): The name of the player.

    Returns:
        dict or None: A dictionary with players points(pts), rebounds(RBS), and assists (AST),
        or no stats.
    """
    player_data = df[(df['Team'] == team) & (df['Player'] == player)]
    if not player_data.empty:
        return {
            "PTS": player_data['PTS'].iloc[0],
            "TRB": player_data['TRB'].iloc[0],
            "AST": player_data['AST'].iloc[0]
        }
    return None