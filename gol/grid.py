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
    start_position = None
    offset = Vector(0, 0)
    rect_size = 25
    width = 20
    height = 15
    occupied_fill = "#000000"
    dead_fill = "#ffffff"
    outline_color = "#c1c1c1"
    to_delete = []

    def __init__(self, canvas: Canvas, rect_size: int = 25):
        self.canvas = canvas
        self.rect_size = rect_size
        self.state = [[States.DEAD for y in range(self.height)] for x in range(self.width)]
        self.game_state = []
        self.moving = False
        self.canvas.bind("<Button-1>", self.update)
        self.canvas.bind("<Control-Button-4>", self.zoom)
        self.canvas.bind("<Control-Button-5>", self.zoom)
        self.canvas.bind("<Control-Button-1>", self.enable_moving)
        self.canvas.bind("<Control-ButtonRelease-1>", self.disable_moving)
        self.canvas.bind("<Control-B1-Motion>", self.move_grid)

    def move_grid(self, event: Event):
        self.offset.x += (event.x - self.start_position.x)
        self.offset.y += (event.y - self.start_position.y)
        self.start_position = Vector(event.x, event.y)
        self.redraw()

    def enable_moving(self, event: Event):
        self.start_position = Vector(event.x, event.y)

    def disable_moving(self, event: Event):
        self.start_position = Vector(0, 0)

    def zoom(self, event: Event):
        if self.start_position is None:
            self.enable_moving(event)

        if event.num == 4 and self.rect_size < 50:
            self.rect_size = round(self.rect_size * 1.1)

        elif self.rect_size > 10:
            self.rect_size = round(self.rect_size * 0.9)

        if self.rect_size > 50:
            self.rect_size = 50

        if self.rect_size < 10:
            self.rect_size = 10

        self.redraw()

    def draw(self):
        for x in range(round(int(self.canvas['width']) / self.rect_size)):
            for y in range(round(int(self.canvas['height']) / self.rect_size)):
                new_x = x - floor(self.offset.x / self.rect_size)
                new_y = y - floor(self.offset.y / self.rect_size)

                if Vector(new_x, new_y) in self.game_state:
                    fill = self.occupied_fill
                else:
                    fill = self.dead_fill

                self.to_delete.append(self.canvas.create_rectangle(
                    x * self.rect_size,
                    y * self.rect_size,
                    (x * self.rect_size) + self.rect_size,
                    (y * self.rect_size) + self.rect_size,
                    outline=self.outline_color,
                    fill=fill
                ))

    def update(self, event: Event) -> None:
        x = floor(event.x / self.rect_size)
        y = floor(event.y / self.rect_size)

        new_x = x - floor(self.offset.x / self.rect_size)
        new_y = y - floor(self.offset.y / self.rect_size)
        clicked_vector = Vector(new_x, new_y)

        if clicked_vector in self.game_state:
            self.game_state.remove(clicked_vector)
        else:
            self.game_state.append(clicked_vector)

        self.redraw()

    def redraw(self) -> None:
        current_items = self.canvas.find_all()
        self.draw()

        for item in current_items:
            self.canvas.delete(item)
