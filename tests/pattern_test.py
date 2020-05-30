import unittest

from gol.game import Game
from gol.grid import Vector


# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

class StillLifeTest(unittest.TestCase):

    def _still_life_comparison(self, starting_board: list):
        game = Game(starting_board.copy())
        new_board = game.update()

        self.assertEqual(
            sorted(starting_board, key=lambda position: (position.x, position.y)),
            sorted(new_board, key=lambda position: (position.x, position.y))
        )

    def test_block(self):
        self._still_life_comparison([
            Vector(0, 0),
            Vector(0, 1),
            Vector(1, 0),
            Vector(1, 1)
        ])

    def test_beehive(self):
        self._still_life_comparison([
            Vector(0, 1),
            Vector(1, 0),
            Vector(2, 0),
            Vector(3, 1),
            Vector(1, 2),
            Vector(2, 2)
        ])

    def test_loaf(self):
        self._still_life_comparison([
            Vector(0, 1),
            Vector(1, 0),
            Vector(2, 0),
            Vector(3, 1),
            Vector(1, 2),
            Vector(2, 3),
            Vector(3, 2)
        ])

    def test_boat(self):
        self._still_life_comparison([
            Vector(0, 0),
            Vector(0, 1),
            Vector(1, 0),
            Vector(1, 2),
            Vector(2, 1),
        ])

    def test_tub(self):
        self._still_life_comparison([
            Vector(0, 1),
            Vector(1, 0),
            Vector(1, 2),
            Vector(2, 1),
        ])


class OscillatorsTest(unittest.TestCase):

    def _oscillator_comparison(self, starting_board: list, period: int):
        game = Game(starting_board.copy())
        new_board = starting_board.copy()

        for step in range(period):
            new_board = game.update()

        self.assertEqual(
            sorted(starting_board, key=lambda position: (position.x, position.y)),
            sorted(new_board, key=lambda position: (position.x, position.y))
        )

    def test_blinker(self):
        self._oscillator_comparison([
            Vector(0, 1),
            Vector(1, 1),
            Vector(2, 1)
        ], 2)

    def test_toad(self):
        self._oscillator_comparison([
            Vector(1, 0),
            Vector(2, 0),
            Vector(3, 0),
            Vector(0, 1),
            Vector(1, 1),
            Vector(2, 1),
        ], 2)

    def test_beacon(self):
        self._oscillator_comparison([
            Vector(0, 0),
            Vector(0, 1),
            Vector(1, 0),
            Vector(2, 3),
            Vector(3, 2),
            Vector(3, 3),
        ], 2)

    # TODO: Pulsar & Penta-decathlon


class SpaceshipTest(unittest.TestCase):
    def _spaceship_comparison(self, starting_board: list, period: int, offset: Vector):
        game = Game(starting_board.copy())
        new_board = starting_board.copy()

        for step in range(period):
            new_board = game.update()

        expected_board = [position + offset for position in starting_board]

        self.assertEqual(
            sorted(expected_board, key=lambda position: (position.x, position.y)),
            sorted(new_board, key=lambda position: (position.x, position.y))
        )

    def test_glider(self):
        self._spaceship_comparison([
            Vector(1, 0),
            Vector(0, 2),
            Vector(1, 2),
            Vector(2, 2),
            Vector(2, 1),
        ], 4, Vector(1, 1))

    def test_lwss(self):
        self._spaceship_comparison([
            Vector(0, 0),
            Vector(3, 0),
            Vector(4, 1),
            Vector(4, 2),
            Vector(4, 3),
            Vector(3, 3),
            Vector(2, 3),
            Vector(1, 3),
            Vector(0, 2)
        ], 4, Vector(2, 0))

    def test_mwss(self):
        self._spaceship_comparison([
            Vector(2, 0),
            Vector(0, 1),
            Vector(4, 1),
            Vector(5, 2),
            Vector(5, 3),
            Vector(5, 4),
            Vector(4, 4),
            Vector(3, 4),
            Vector(2, 4),
            Vector(1, 4),
            Vector(0, 3)
        ], 4, Vector(2, 0))

    def test_hwss(self):
        self._spaceship_comparison([
            Vector(0, 1),
            Vector(0, 3),
            Vector(2, 0),
            Vector(3, 0),
            Vector(5, 1),
            Vector(6, 2),
            Vector(6, 3),
            Vector(5, 4),
            Vector(4, 4),
            Vector(3, 4),
            Vector(1, 4),
            Vector(2, 4),
            Vector(6, 4)
        ], 4, Vector(2, 0))


if __name__ == '__main__':
    unittest.main()
