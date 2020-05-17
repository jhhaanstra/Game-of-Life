import tkinter as tk

from Grid import Grid


class Application(tk.Frame):

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
        self.start_button["text"] = "Start"
        self.start_button["command"] = self.start
        self.start_button.pack(side="left", padx=5, pady=5)

        self.stop_button = tk.Button(self)
        self.stop_button["text"] = "Stop"
        self.stop_button["command"] = self.stop
        self.stop_button.pack(side="left", padx=5, pady=5)

        self.close = tk.Button(self, text="close", command=self.master.destroy)
        self.close.pack(side="left", padx=5, pady=5)

    def start(self):
        print("Started")

    def stop(self):
        print("Stopped")

root = tk.Tk()
app = Application(master=root)
app.mainloop()