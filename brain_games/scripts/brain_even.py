#!/usr/bin/env python

from brain_games.game_engine import start_the_game
from brain_games.games import even


def main():
    start_the_game(even)


if __name__ == '__main__':
    main()
