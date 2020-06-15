import tkinter as tk
from threading import Thread
from time import sleep

from gol.game import Game
from gol.grid import Grid


class Application(tk.Frame):
    game = None
    game_thread = None
    game_interval = 1 / 50

    def __init__(self, master=None):
        super().__init__(master)
        self.close = tk.Button(self, text="Close", command=self.quit)
        self.canvas = tk.Canvas(self, width="20c", height="10c", offset="")
        self.start_button = tk.Button(self, text="Start", command=self.start)
        self.stop_button = tk.Button(self, text="Stop", command=self.stop, state="disabled")
        self.reset_button = tk.Button(self, text="Reset", command=self.reset)
        self.speed_scale = tk.Scale(self, from_=1, to=100, orient=tk.HORIZONTAL, command=self.update_game_interval)
        self.master = master

        self.pack()
        self.pack_widgets()
        self.grid = Grid(self.canvas)
        self.grid.draw()

    def pack_widgets(self):
        self.canvas.pack(side="top", padx=5, pady=5)
        self.start_button.pack(side="left", padx=5, pady=5)
        self.stop_button.pack(side="left", padx=5, pady=5)
        self.reset_button.pack(side="left", padx=5, pady=5)
        self.close.pack(side="left", padx=5, pady=5)
        self.speed_scale.pack(side="top", padx=5, pady=5)

    def update_game_interval(self, event: tk.Event):
        self.game_interval = int(event) / 50
        if self.game:
            self.game.interval = self.game_interval

    def start(self):
        self.stop_button["state"] = "normal"
        self.start_button["state"] = "disabled"
        self.reset_button["state"] = "disabled"

        self.game = Game(self.grid.game_state, self.game_interval)
        self.game.is_running = True
        self.game_thread = Thread(target=self.play)
        self.game_thread.start()

    def play(self):
        while self.game.is_running:
            new_state = self.game.update()
            self.grid.game_state = new_state
            self.grid.redraw()
            sleep(self.game.interval)

    def stop(self):
        self.game.is_running = False
        self.game_thread.join()

        self.stop_button["state"] = "disabled"
        self.start_button["state"] = "normal"
        self.reset_button["state"] = "normal"

    def reset(self):
        self.grid.game_state = []
        self.grid.redraw()

    def quit(self):
        if self.game and self.game.is_running:
            self.stop()

        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
