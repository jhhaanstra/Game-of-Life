from math import floor

from Game import States
from tkinter import Canvas, Event


class Grid(object):
    canvas = None
    rect_size = 25
    width = 20
    height = 15
    state = []
    occupied_fill = "#2f3eb5"
    vacant_fill = "#c0e5e5"
    outline_color = "#ced1e8"

    def __init__(self, canvas: Canvas, rect_size: int = 25):
        self.canvas = canvas
        self.rect_size = rect_size
        self.state = [[States.VACANT for y in range(self.height)] for x in range(self.width)]
        self.canvas.bind("<Button-1>", self.update)

    def draw(self):
        for x_count, row in enumerate(self.state):
            for y_count, col in enumerate(row):
                self.canvas.create_rectangle(
                    x_count * self.rect_size,
                    y_count * self.rect_size,
                    (x_count * self.rect_size) + self.rect_size,
                    (y_count * self.rect_size) + self.rect_size,
                    outline=self.outline_color,
                    fill=self.occupied_fill if col == States.ALIVE else self.vacant_fill
                )

    def update(self, event: Event):
        x_coord = floor(event.x / self.rect_size)
        y_coord = floor(event.y / self.rect_size)
        try:
            cell_to_update = self.state[x_coord][y_coord]
            self.state[x_coord][y_coord] = States.ALIVE if cell_to_update == States.VACANT else States.VACANT
            self.redraw()
        except IndexError:
            pass

    def redraw(self):
        self.canvas.delete("all")
        self.draw()
