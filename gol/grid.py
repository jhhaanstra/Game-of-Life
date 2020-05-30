from enum import Enum
from math import floor

from tkinter import Canvas, Event


class States(Enum):
    DEAD = 1
    ALIVE = 2


class Vector(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def as_coord(self) -> tuple:
        return self.x, self.y

    def __add__(self, other):
        total_x = self.x + other.x
        total_y = self.y + other.y
        return Vector(total_x, total_y)

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self) -> str:
        return "[{}, {}]".format(self.x, self.y)


class Cell(object):
    def __init__(self, vector: object, state: States):
        self.vector = vector
        self.state = state


class Grid(object):
    canvas = None
    rect_size = 25
    width = 20
    height = 15
    occupied_fill = "#2f3eb5"
    dead_fill = "#c0e5e5"
    outline_color = "#ced1e8"

    def __init__(self, canvas: Canvas, rect_size: int = 25):
        self.canvas = canvas
        self.rect_size = rect_size
        self.state = [[States.DEAD for y in range(self.height)] for x in range(self.width)]
        self.game_state = []
        self.canvas.bind("<Button-1>", self.update)

    def draw(self):
        for x in range(self.width):
            for y in range(self.height):
                if Vector(x, y) in self.game_state:
                    fill = self.occupied_fill
                else:
                    fill = self.dead_fill

                self.canvas.create_rectangle(
                    x * self.rect_size,
                    y * self.rect_size,
                    (x * self.rect_size) + self.rect_size,
                    (y * self.rect_size) + self.rect_size,
                    outline=self.outline_color,
                    fill=fill
                )

    def update(self, event: Event) -> None:
        x = floor(event.x / self.rect_size)
        y = floor(event.y / self.rect_size)
        clicked_vector = Vector(x, y)

        if clicked_vector in self.game_state:
            self.game_state.remove(clicked_vector)
        else:
            self.game_state.append(clicked_vector)

        self.redraw()

    def redraw(self) -> None:
        self.canvas.delete("all")
        self.draw()
