import sys
import pygame
print("pygame module:", pygame)
print("has init:", hasattr(pygame, "init"))
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
import asyncio

from src.core_game import Game



async def main():
    game = Game()

    while game.running:
        game.tick()
        await asyncio.sleep(0)

    game.quit()


if __name__ == "__main__":
    asyncio.run(main())
