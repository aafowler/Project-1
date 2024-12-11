from nbagui import *

def main(): 
    master = tk.Tk()
    master.title('NBA Player Stats')
    master.geometry('210x240')
    NBAStatsGUI(master)
    master.mainloop()

if __name__ == '__main__':
    main()