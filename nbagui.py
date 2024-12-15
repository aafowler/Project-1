import tkinter as tk
from tkinter import ttk
from typing import Dict, List, Tuple, Any
from nbalogic import get_data, get_players, get_stats
import pandas as pd

class NBAStatsGUI:
    """
        Initializes the NBAStatsGUI with necessary components.

        Args:
            master (tk.Tk): Is the window of the app.
    """
    def __init__(self, master: tk.Tk):
        self.master = master
        self.df: pd.DataFrame = get_data()
        self.team_players: Dict[str, List[str]] = get_players(self.df)
        self.team_players_sorted: List[str] = sorted(self.team_players.keys())

        self.header_title = ttk.Label(master, text='NBA STATS', font=('Arial', 16))
        self.header_title.grid(row=0, column=0, columnspan=3, pady=10, padx=45, sticky='nw')

        self.team_abv = tk.StringVar(master)
        self.player_tag = tk.StringVar(master)

        self.team_name = ttk.Label(master, text='Team:')
        self.team_name.grid(row=1, column=0, padx=5, pady=5, sticky='w')

        self.team_dropdown = ttk.Combobox(master, textvariable=self.team_abv, values=self.team_players_sorted)
        self.team_dropdown.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        self.team_dropdown.bind('<<ComboboxSelected>>', self.update_player_dropdown)

        self.player_name = ttk.Label(master, text='Player:')
        self.player_name.grid(row=2, column=0, padx=5, pady=5, sticky='w')

        self.player_dropdown = ttk.Combobox(master, textvariable=self.player_tag)
        self.player_dropdown.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        self.player_dropdown.bind('<<ComboboxSelected>>', self.display_stats)

        self.points_label = ttk.Label(master, text='PTS:')
        self.points_label.grid(row=3, column=1, padx=5, pady=5, sticky='w')

        self.rebounds_label = ttk.Label(master, text='TRB:')
        self.rebounds_label.grid(row=4, column=1, padx=5, pady=5, sticky='w')

        self.assists_label = ttk.Label(master, text='AST:')
        self.assists_label.grid(row=5, column=1, padx=5, pady=5, sticky='w')

        self.reset_button = ttk.Button(master, text='Reset', command=self.reset_gui)
        self.reset_button.grid(row=6, column=0, columnspan=2, pady=10)

    def update_player_dropdown(self, *args: Any):
        """
        Updates dropdown to the selected team.
        """
        selected_team: str = self.team_abv.get()
        self.player_dropdown['values'] = self.team_players.get(selected_team, [])
        self.player_tag.set('')
        self.points_label.config(text='PTS:')
        self.rebounds_label.config(text='TRB:')
        self.assists_label.config(text='AST:')

    def display_stats(self, *args: Any):
        """
        Updates stats variable labels.
        """
        selected_team: str = self.team_abv.get()
        selected_player: str = self.player_tag.get()
        stats: Dict[str, Any] = get_stats(self.df, selected_team, selected_player)
        if stats:
            self.points_label.config(text=f'PTS: {stats["PTS"]}')
            self.rebounds_label.config(text=f'TRB: {stats["TRB"]}')
            self.assists_label.config(text=f'AST: {stats["AST"]}')
        else:
            self.points_label.config(text='PTS: Not Found')
            self.rebounds_label.config(text='TRB: Not Found')
            self.assists_label.config(text='AST: Not Found')

    def reset_gui(self):
        """
        Clears GUI
        """
        self.team_abv.set('')
        self.player_tag.set('')
        self.player_dropdown['values'] = []
        self.points_label.config(text='PTS:')
        self.rebounds_label.config(text='TRB:')
        self.assists_label.config(text='AST:')