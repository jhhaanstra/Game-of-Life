from copy import deepcopy
from enum import Enum
from itertools import permutations


class States(Enum):
    DEAD = 1
    ALIVE = 2
    VACANT = 3


class Game(object):
    interval = 1
    running = True
    state = []
    width = 20
    height = 15

    def __init__(self, state: list):
        self.state = state

    def update(self) -> list:
        new_state = deepcopy(self.state)

        for x_count, row in enumerate(self.state):
            for y_count, col in enumerate(row):
                living_neighbours_count = 0

                for neighbour in permutations(range(-1, 2), 2):
                    if self.is_alive(x_count + neighbour[0], y_count + neighbour[1]):
                        living_neighbours_count += 1

                for i in [-1, 1]:
                    if self.is_alive(x_count + i, y_count + i):
                        living_neighbours_count += 1

                if living_neighbours_count > 0:
                    print("[{x}, {y}] has living_neighbours_alive: {count}".format(
                        x=x_count,
                        y=y_count,
                        count=living_neighbours_count
                    ))

                if self.state[x_count][y_count] == States.ALIVE and (living_neighbours_count < 2 or living_neighbours_count > 3):
                    new_state[x_count][y_count] = States.DEAD

        self.state = new_state

        return self.state

    def is_alive(self, x, y) -> bool:
        try:
            return (self.state[x][y] == States.ALIVE)
            return False
        except IndexError:
            pass





