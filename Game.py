from copy import deepcopy
from itertools import permutations

from Grid import States, Vector


class Game(object):

    NEIGHBOURING_POSITIONS = [
        Vector(1, 0),
        Vector(0, 1),
        Vector(1, 1),
        Vector(-1, 0),
        Vector(0, -1),
        Vector(-1, -1)
    ]

    interval = 1
    running = True
    game_state = {}
    dead_cells = []
    width = 20
    height = 15

    def __init__(self, state: list):
        self.state = state
        for x in range(self.width):
            for y in range(self.height):
                if self.state[x][y] != States.VACANT:
                    self.game_state[Vector(x, y)] = self.state[x][y]

    def update(self) -> dict:
        new_state = {}

        for position, state in self.game_state.items():
            living_neighbours_count = 0
            for neighbour in self.NEIGHBOURING_POSITIONS:
                neighbouring_position = (position + neighbour)
                if neighbouring_position in self.game_state:
                    if self.game_state[neighbouring_position] == States.ALIVE:
                        living_neighbours_count += 1

            if living_neighbours_count > 0:
                print("{position} has living_neighbours_alive: {count}".format(
                    position=str(position),
                    count=living_neighbours_count
                ))

            # - Any live cell with fewer than two live neighbours dies, as if by underpopulation.
            # - Any live cell with more than three live neighbours dies, as if by overpopulation.
            if state == States.ALIVE and (living_neighbours_count < 2 or living_neighbours_count > 3):
                new_state[position] = States.DEAD
            # - Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
            elif state == States.DEAD and living_neighbours_count == 3:
                new_state[position] = States.ALIVE
            # - Any live cell with two or three live neighbours lives on to the next generation.
            else:
                new_state[position] = state

        self.game_state = new_state
        return self.game_state
