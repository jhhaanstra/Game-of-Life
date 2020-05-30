import unittest

from gol.game import Game
from gol.grid import Vector


class TestGameStateUpdateStillLife(unittest.TestCase):

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


class GameStateUpdateOscillators(unittest.TestCase):

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
