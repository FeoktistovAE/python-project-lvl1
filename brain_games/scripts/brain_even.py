#!/usr/bin/env python

from brain_games.game_engine import start
from brain_games.games import even


def main():
    start(even)


if __name__ == '__main__':
    main()
