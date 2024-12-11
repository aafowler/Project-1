from nba import *
import tkinter as tk
from tkinter import ttk

class NBAStatsGUI:
    def __init__(self, master):
        self.master = master
        self.df = pd.read_csv('nba_2025_stats.csv')
        self.header_title = ttk.Label(master, text='NBA STATS', font=('Arial', 16))
        self.header_title.grid(row=0, column=0, columnspan=3, pady=10, padx=45, sticky='nw')

        self.team_abv = tk.StringVar(master)
        self.player_tag = tk.StringVar(master)

        self.team_name = ttk.Label(master, text='Team:')
        self.team_name.grid(row=1, column=0, padx=5, pady=5, sticky = 'w')

        self.team_dropdown = ttk.Combobox(master, textvariable=self.team_abv, values=list(team_players_sorted))
        self.team_dropdown.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        self.team_dropdown.bind('<<ComboboxSelected>>', self.update_player_dropdown)

        self.player_name = ttk.Label(master, text='Player:')
        self.player_name.grid(row=2, column=0, padx=5, pady=5, sticky='w')

        self.player_dropdown = ttk.Combobox(master, textvariable=self.player_tag)
        self.player_dropdown.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        self.player_dropdown.bind('<<ComboboxSelected>>', self.display_stats)

        self.points_label = ttk.Label(master, text='PTS:')
        self.points_label.grid(row=3, column=1, padx=5, pady=5, sticky='w')

        self.rebounds_label = ttk.Label(master, text='RBS:')
        self.rebounds_label.grid(row=4, column=1, padx=5, pady=5, sticky='w')

        self.assists_label = ttk.Label(master, text='AST:')
        self.assists_label.grid(row=5, column=1, padx=5, pady=5, sticky='w')

        self.reset_button = ttk.Button(master, text='Reset', command=self.reset_gui)
        self.reset_button.grid(row=6, column=0, columnspan=2, pady=10)

    def update_player_dropdown(self, *args):
        selected_team = self.team_abv.get()
        self.player_dropdown['values'] = team_players.get(selected_team, [])
        self.player_tag.set('')
        self.points_label.config(text='PTS:')
        self.rebounds_label.config(text='RBS:')
        self.assists_label.config(text='AST:')

    def display_stats(self, *args):
        selected_team = self.team_abv.get()
        selected_player = self.player_tag.get()

        try:
            player_data = self.df[(self.df['Team'] == selected_team) & (self.df['Player'] == selected_player)]
            if not player_data.empty:
                points = player_data['PTS'].iloc[0]
                rebounds = player_data['TRB'].iloc[0]
                assists = player_data['AST'].iloc[0]

                self.points_label.config(text=f'PTS: {points}')
                self.rebounds_label.config(text=f'RBS: {rebounds}')
                self.assists_label.config(text=f'AST: {assists}')
            else:
                self.points_label.config(text='PTS: Not Found')
                self.rebounds_label.config(text='RBS: Not Found')
                self.assists_label.config(text='AST: Not Found')
        except (IndexError, KeyError):
            self.points_label.config(text='PTS: Error')
            self.rebounds_label.config(text='RBS: Error')
            self.assists_label.config(text='AST: Error')

    def reset_gui(self):
        self.team_abv.set('')
        self.player_tag.set('')
        self.player_dropdown['values'] = []
        self.points_label.config(text='PTS:')
        self.rebounds_label.config(text='TRB:')
        self.assists_label.config(text='AST:')