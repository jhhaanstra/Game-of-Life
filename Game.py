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
        Vector(-1, -1),
        Vector(-1, 1),
        Vector(1, -1)
    ]

    interval = 1
    running = True
    game_state = []
    width = 20
    height = 15

    def __init__(self, state: list):
        self.state = state
        for x in range(self.width):
            for y in range(self.height):
                if self.state[x][y] != States.DEAD:
                    self.game_state[Vector(x, y)] = self.state[x][y]

    def update(self) -> list:
        new_state = []
        neighbours = {}

        for position in self.game_state:
            living_neighbours_count = 0

            # if state == States.DEAD:
            #     print("test")

            for neighbour in self.NEIGHBOURING_POSITIONS:
                neighbouring_position = position + neighbour
                if neighbouring_position in self.game_state:
                    living_neighbours_count += 1

                if neighbouring_position not in neighbours:
                    neighbours[neighbouring_position] = 0
                else:
                    neighbours[neighbouring_position] += 1

            if living_neighbours_count > 0:
                print("{position} has living_neighbours_alive: {count}".format(
                    position=str(position),
                    count=living_neighbours_count
                ))

            # # - Any live cell with fewer than two live neighbours dies, as if by underpopulation.
            # # - Any live cell with more than three live neighbours dies, as if by overpopulation.
            # if living_neighbours_count < 2 or living_neighbours_count > 3:
            #     pass

            # - Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
            if living_neighbours_count == 3:
                new_state.append(position)

            # # - Any live cell with two or three live neighbours lives on to the next generation.
            # else:
            #     new_state.append(position)

        for neighbouring_position, count in neighbours.items():
            if count == 3:
                new_state.append(neighbouring_position)

        self.game_state = new_state
        return self.game_state
