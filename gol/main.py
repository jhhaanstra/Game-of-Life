import tkinter as tk
from threading import Thread
from time import sleep

from gol.game import Game
from gol.grid import Grid


class Application(tk.Frame):
    game = None
    game_thread = None

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.pack()
        self.create_widgets()
        self.grid = Grid(self.canvas)
        self.grid.draw()

    def create_widgets(self):
        self.canvas = tk.Canvas(self)
        self.canvas["width"] = "20c"
        self.canvas["height"] = "10c"
        self.canvas["offset"] = ""
        self.canvas.pack(side="top", padx=5, pady=5)

        self.start_button = tk.Button(self)
        self.start_button["text"] = "Step"
        self.start_button["command"] = self.start
        self.start_button.pack(side="left", padx=5, pady=5)

        self.stop_button = tk.Button(self)
        self.stop_button["text"] = "Stop"
        self.stop_button["command"] = self.stop
        self.stop_button["state"] = "disabled"
        self.stop_button.pack(side="left", padx=5, pady=5)

        self.reset_button = tk.Button(self)
        self.reset_button["text"] = "Reset grid"
        self.reset_button["command"] = self.reset
        self.reset_button.pack(side="left", padx=5, pady=5)


        self.close = tk.Button(self, text="close", command=self.master.destroy)
        self.close.pack(side="left", padx=5, pady=5)

    def start(self):
        self.game = Game(self.grid.game_state)
        self.game.running = True
        self.game_thread = Thread(target=self.play)
        self.game_thread.start()

    def play(self):
        while self.game.running:
            new_state = self.game.update()
            self.stop_button["state"] = "normal"
            self.start_button["state"] = "disabled"
            self.reset_button["state"] = "disabled"

            # self.grid.state = new_state
            self.grid.game_state = new_state
            self.grid.redraw()
            sleep(self.game.interval)

    def stop(self):
        self.game.running = False
        self.game_thread.join()
        self.start_button["state"] = "normal"
        self.stop_button["state"] = "disabled"
        self.reset_button["state"] = "normal"

    def reset(self):
        self.grid.game_state = []
        self.grid.redraw()



root = tk.Tk()
app = Application(master=root)
app.mainloop()
