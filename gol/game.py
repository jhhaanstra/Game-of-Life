from gol.grid import Vector


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
        self.game_state = state

    def update(self) -> list:
        new_state = []
        neighbours = {}

        for position in self.game_state:
            living_neighbours_count = 0

            for neighbour in self.NEIGHBOURING_POSITIONS:
                neighbouring_position = position + neighbour
                if neighbouring_position in self.game_state:
                    living_neighbours_count += 1

                if neighbouring_position not in self.game_state:
                    if neighbouring_position not in neighbours:
                        neighbours[neighbouring_position] = 1
                    else:
                        neighbours[neighbouring_position] += 1

            if living_neighbours_count == 3 or living_neighbours_count == 2:
                new_state.append(position)

        for position, count in neighbours.items():
            if count == 3:
                new_state.append(position)

        self.game_state = new_state
        return self.game_state
